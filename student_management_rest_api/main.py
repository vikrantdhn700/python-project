from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Student Management API")

students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 20,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 21,
        "course": "Data Science"
    },
    {
        "id": 3,
        "name": "Amit",
        "age": 22,
        "course": "FastAPI"
    }
]


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=10, le=100)
    course: str = Field(min_length=2, max_length=100)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=50
    )
    age: Optional[int] = Field(
        default=None,
        gt=0,
        le=100
    )
    course: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

# Get students


@app.get("/students")
def get_students():
    if not students:
        raise HTTPException(
            status_code=404,
            detail="Students not found"
        )

    return {
        "status": "success",
        "message": "Students found",
        "data": students
    }


# Get student by id

@app.get("/students/{id}")
def get_student(id: int):
    if not isinstance(id, int):
        raise HTTPException(
            status_code=404,
            detail="Invalid parameter: expected int"
        )

    student = find_student(id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "status": "success",
        "message": "Student found",
        "data": student
    }

# Add new student


@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    if len(students) == 0:
        new_id = 1
    else:
        new_id = max(student["id"] for student in students) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)
    return {
        "status": "success",
        "message": "Student created successfully",
        "data": new_student
    }

# Replace student


@app.put("/students/{id}")
def replace_student(id: int, student: StudentUpdate):
    if not isinstance(id, int):
        raise HTTPException(
            status_code=404,
            detail="Invalid parameter: expected int"
        )

    existing_student = find_student(id)
    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    existing_student["name"] = student.name
    existing_student["age"] = student.age
    existing_student["course"] = student.course

    return {
        "status": "success",
        "message": "Student successfully replace",
        "data": existing_student
    }

# Update student


@app.patch("/students/{id}")
def update_student(id: int, student: StudentUpdate):
    if not isinstance(id, int):
        raise HTTPException(
            status_code=404,
            detail="Invalid parameter: expected int"
        )

    existing_student = find_student(id)

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        existing_student[field] = value

    return {
        "status": "success",
        "message": "Student successfully updated",
        "data": existing_student
    }

# Delete student


@app.delete("/students/{id}")
def delete_student(id: int):
    if not isinstance(id, int):
        raise HTTPException(
            status_code=404,
            detail="Invalid parameter: expected int"
        )

    existing_student = find_student(id)

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    students.remove(existing_student)
    return {
        "status": "success",
        "message": "Student deleted successfully",
        "data": existing_student
    }
