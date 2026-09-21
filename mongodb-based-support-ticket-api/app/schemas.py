from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field

TicketStatus = Literal["open", "in_progress", "resolved", "closed"]
TicketPriority = Literal["low", "medium", "high", "urgent"]


class Customer(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=30)


class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, max_length=30)


class CommentCreate(BaseModel):
    author: str = Field(min_length=2, max_length=100)
    message: str = Field(min_length=1, max_length=2000)


class Comment(CommentCreate):
    created_at: datetime


class TicketCreate(BaseModel):
    customer: Customer
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5, max_length=5000)
    category: str = Field(min_length=2, max_length=50)
    priority: TicketPriority = "medium"
    tags: list[str] = Field(default_factory=list)


class TicketUpdate(BaseModel):
    customer: Optional[CustomerUpdate] = None
    title: Optional[str] = Field(default=None, min_length=3, max_length=200)
    description: Optional[str] = Field(
        default=None, min_length=5, max_length=5000)
    category: Optional[str] = Field(default=None, min_length=2, max_length=50)
    priority: Optional[TicketPriority] = None
    tags: Optional[list[str]] = None


class StatusUpdate(BaseModel):
    status: TicketStatus


class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    customer: Customer
    title: str
    description: str
    category: str
    priority: TicketPriority
    status: TicketStatus
    comments: list[Comment]
    tags: list[str]
    created_at: datetime
    updated_at: datetime
