from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Status = Literal["pending", "in_progress", "completed"]


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=255)


class UserResponse(UserCreate):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = None


class ProjectResponse(ProjectCreate):
    id: str
    created_at: datetime


class TaskCreate(BaseModel):
    project_id: str
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None


class TaskResponse(BaseModel):
    id: str
    project_id: str
    title: str
    description: str | None
    status: Status
    assigned_to: str | None
    created_at: datetime


class AssignTask(BaseModel):
    assigned_to: str


class UpdateStatus(BaseModel):
    status: Status
