import re
from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId
from fastapi import FastAPI, HTTPException, Query, status

from app.database import tickets_collection
from app.schemas import CommentCreate, StatusUpdate, TicketCreate, TicketPriority, TicketResponse, TicketStatus, TicketUpdate

app = FastAPI(title="Customer Support Ticket API", version="1.0.0")


def ticket_response(ticket: dict) -> dict:
    """Convert MongoDB's ObjectId to a JSON-friendly id."""
    ticket["id"] = str(ticket.pop("_id"))
    return ticket


def ticket_id_or_404(ticket_id: str) -> ObjectId:
    if not ObjectId.is_valid(ticket_id):
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ObjectId(ticket_id)


@app.post("/tickets", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(ticket: TicketCreate):
    now = datetime.now(timezone.utc)
    document = ticket.model_dump()
    document.update({
        "status": "open",
        "comments": [],
        "created_at": now,
        "updated_at": now,
    })
    result = tickets_collection.insert_one(document)
    document["_id"] = result.inserted_id
    return ticket_response(document)


@app.get("/tickets", response_model=list[TicketResponse])
def get_tickets(
    priority: Optional[TicketPriority] = None,
    status: Optional[TicketStatus] = None,
    category: Optional[str] = None,
    search: Optional[str] = Query(default=None, min_length=1),
):
    filters: dict = {}
    if priority:
        filters["priority"] = priority
    if status:
        filters["status"] = status
    if category:
        filters["category"] = category
    if search:
        safe_search = re.escape(search)
        filters["$or"] = [
            {"title": {"$regex": safe_search, "$options": "i"}},
            {"description": {"$regex": safe_search, "$options": "i"}},
            {"customer.name": {"$regex": safe_search, "$options": "i"}},
            {"tags": {"$regex": safe_search, "$options": "i"}},
        ]

    tickets = tickets_collection.find(filters).sort("created_at", -1)
    return [ticket_response(ticket) for ticket in tickets]


@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: str):
    ticket = tickets_collection.find_one({"_id": ticket_id_or_404(ticket_id)})
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket_response(ticket)


@app.patch("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: str, ticket: TicketUpdate):
    update_data = ticket.model_dump(exclude_none=True)
    if update_data:
        update_data["updated_at"] = datetime.now(timezone.utc)
        tickets_collection.update_one(
            {"_id": ticket_id_or_404(ticket_id)},
            {"$set": update_data},
        )

    updated_ticket = tickets_collection.find_one(
        {"_id": ticket_id_or_404(ticket_id)})
    if updated_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket_response(updated_ticket)


@app.patch("/tickets/{ticket_id}/status", response_model=TicketResponse)
def change_status(ticket_id: str, status_data: StatusUpdate):
    updated_ticket = tickets_collection.find_one_and_update(
        {"_id": ticket_id_or_404(ticket_id)},
        {"$set": {"status": status_data.status,
                  "updated_at": datetime.now(timezone.utc)}},
        return_document=True,
    )
    if updated_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket_response(updated_ticket)


@app.post("/tickets/{ticket_id}/comments", response_model=TicketResponse)
def add_comment(ticket_id: str, comment: CommentCreate):
    new_comment = comment.model_dump()
    new_comment["created_at"] = datetime.now(timezone.utc)
    updated_ticket = tickets_collection.find_one_and_update(
        {"_id": ticket_id_or_404(ticket_id)},
        {
            "$push": {"comments": new_comment},
            "$set": {"updated_at": datetime.now(timezone.utc)},
        },
        return_document=True,
    )
    if updated_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket_response(updated_ticket)


@app.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: str):
    result = tickets_collection.delete_one(
        {"_id": ticket_id_or_404(ticket_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Deleted succesffuly"}
