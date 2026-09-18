from datetime import datetime
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime


class StudentListRead(BaseModel):
    status: str
    message: str
    data: list[StudentRead]


class StudentCreate(BaseModel):
    first_name: str = Field(min_length=2, max_length=100)
    last_name: str = Field(min_length=2, max_length=100)
    email: EmailStr


class StudentUpdate(BaseModel):
    first_name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    last_name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    email: Optional[EmailStr] = None


class CourseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    code: str
    title: str
    description: str
    credit_hours: int
    price: Decimal


class CourseListRead(BaseModel):
    status: str
    message: str
    data: list[CourseRead]


class CourseCreate(BaseModel):
    code: str = Field(min_length=2, max_length=20, pattern=r"^[A-Za-z0-9-]+$")
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    credit_hours: int = Field(default=3, ge=1, le=12)
    price: Decimal = Field(ge=0.00, max_digits=10, decimal_places=2)


class CourseUpdate(BaseModel):
    code: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=20,
        pattern=r"^[A-Za-z0-9-]+$"
    )
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    credit_hours: Optional[int] = Field(default=None, ge=1, le=12)
    price: Optional[Decimal] = Field(
        default=None, ge=0.00, max_digits=10, decimal_places=2)


class EnrollmentRead(BaseModel):
    id: int
    student_name: str
    course_title: str
    enrolled_at: datetime
    status: str


class EnrollmentListRead(BaseModel):
    status: str
    message: str
    data: list[EnrollmentRead]


class EnrollmentCreate(BaseModel):
    student_id: int = Field(gt=0)
    course_id: int = Field(gt=0)


class EnrollmentUpdate(BaseModel):
    status: Optional[str] = Field(default=None, min_length=1, max_length=20)
