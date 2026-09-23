from fastapi import APIRouter, HTTPException, Query, status
from pymongo import ReturnDocument

from ..database import projects_collection, tasks_collection, users_collection
from ..schemas import AssignTask, TaskCreate, TaskResponse, UpdateStatus
from ..utils import parse_object_id, serialize_document, utc_now

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def find_task(task_id: str):
    return tasks_collection.find_one({"_id": parse_object_id(task_id)})


def require_task(task_id: str):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate):
    project_id = parse_object_id(data.project_id)

    if not projects_collection.find_one({"_id": project_id}):
        raise HTTPException(status_code=404, detail="Project not found")

    document = {
        "project_id": project_id,
        "title": data.title,
        "description": data.description,
        "status": "pending",
        "assigned_to": None,
        "created_at": utc_now(),
    }

    result = tasks_collection.insert_one(document)
    document["_id"] = result.inserted_id
    return serialize_document(document)


@router.get("", response_model=list[TaskResponse])
def get_tasks(
    project_id: str | None = Query(default=None),
    status: str | None = Query(default=None),
    assigned_to: str | None = Query(default=None),
):
    query = {}

    if project_id is not None:
        query["project_id"] = parse_object_id(project_id)

    if status is not None:
        if status not in {"pending", "in_progress", "completed"}:
            raise HTTPException(status_code=400, detail="Invalid status")
        query["status"] = status

    if assigned_to is not None:
        query["assigned_to"] = parse_object_id(assigned_to)

    return [
        serialize_document(doc)
        for doc in tasks_collection.find(query).sort("_id", 1)
    ]


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    return serialize_document(require_task(task_id))


@router.patch("/{task_id}/assign", response_model=TaskResponse)
def assign_task(task_id: str, data: AssignTask):
    task_oid = parse_object_id(task_id)
    user_oid = parse_object_id(data.assigned_to)

    if not users_collection.find_one({"_id": user_oid}):
        raise HTTPException(status_code=404, detail="User not found")

    updated = tasks_collection.find_one_and_update(
        {"_id": task_oid},
        {"$set": {"assigned_to": user_oid}},
        return_document=ReturnDocument.AFTER,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")

    return serialize_document(updated)


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_status(task_id: str, data: UpdateStatus):
    updated = tasks_collection.find_one_and_update(
        {"_id": parse_object_id(task_id)},
        {"$set": {"status": data.status}},
        return_document=ReturnDocument.AFTER,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")

    return serialize_document(updated)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    result = tasks_collection.delete_one({"_id": parse_object_id(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
