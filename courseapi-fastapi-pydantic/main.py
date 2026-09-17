from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Course API with FastAPI + Pydantic")

courses = [
    {
        "id": 1,
        "title": "Python for Beginners",
        "description": "Learn Python programming from basics.",
        "price": 999,
        "duration": 30,
        "instructor": "Rahul Sharma",
        "category": "python",
        "rating": 4.5,
        "active": True
    },
    {
        "id": 2,
        "title": "Advanced FastAPI",
        "description": "Build production-ready APIs using FastAPI.",
        "price": 2500,
        "duration": 20,
        "instructor": "Amit Kumar",
        "category": "fastapi",
        "rating": 4.8,
        "active": True
    },
    {
        "id": 3,
        "title": "Django Web Development",
        "description": "Learn backend development with Django.",
        "price": 4500,
        "duration": 45,
        "instructor": "Priya Singh",
        "category": "python",
        "rating": 4.2,
        "active": True
    },
    {
        "id": 4,
        "title": "JavaScript Fundamentals",
        "description": "Learn the fundamentals of JavaScript.",
        "price": 799,
        "duration": 25,
        "instructor": "Vikash Kumar",
        "category": "javascript",
        "rating": 3.9,
        "active": False
    }
]


class CourseCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=500)
    price: float = Field(ge=0)
    duration: int = Field(gt=0)
    instructor: str = Field(min_length=2, max_length=100)
    category: str = Field(min_length=2, max_length=50)
    rating: float = Field(ge=0, le=5)
    active: bool = True


class CourseUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=100)
    description: Optional[str] = Field(
        default=None, min_length=2, max_length=500)
    price: Optional[float] = Field(default=None, ge=0)
    duration: Optional[int] = Field(default=None, gt=0)
    instructor: Optional[str] = Field(
        default=None, min_length=2, max_length=100)
    category: Optional[str] = Field(default=None, min_length=2, max_length=50)
    rating: Optional[float] = Field(default=None, ge=0, le=5)
    active: Optional[bool] = None


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    duration: int
    instructor: str
    category: str
    rating: float
    active: bool


class CourseListResponse(BaseModel):
    status: str
    message: str
    data: list[CourseResponse]


def find_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return course

    return None


# Get Courses
@app.get("/courses/", response_model=CourseListResponse)
def get_courses(
    category: Optional[str] = None,
    min_price: Optional[float] = Query(
        default=None,
        ge=0
    ),
    max_price: Optional[float] = Query(
        default=None,
        gt=0
    ),
    active: Optional[bool] = None
):

    if (min_price is not None
                and max_price is not None
                and min_price > max_price
            ):
        raise HTTPException(
            status_code=400,
            detail="min_price cannot be greater than max_price"
        )

    filtered_courses = courses

    if category is not None:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["category"].lower() == category.lower()
        ]

    if min_price is not None:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["price"] >= min_price
        ]

    if max_price is not None:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["price"] <= max_price
        ]

    if active is not None:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["active"] == active
        ]

    return {
        "status": "success",
        "message": "Courses successfully fetched",
        "data": filtered_courses
    }

# Get course by id


@app.get("/courses/{id}", response_model=CourseListResponse)
def get_course(id: int):
    course = find_course(id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    return {
        "status": "success",
        "message": "Courses successfully fetched",
        "data": [course]
    }

# Create a new course


@app.post("/courses/")
def create_course(course: CourseCreate):
    if len(courses) == 0:
        new_id = 1
    else:
        new_id = max(c["id"] for c in courses) + 1

    new_course = {
        "id": new_id,
        "title": course.title.strip().title(),
        "description": course.description.strip(),
        "price": course.price,
        "duration": course.duration,
        "instructor": course.instructor,
        "category": course.category.strip(),
        "rating": course.rating,
        "active": course.active
    }

    courses.append(new_course)
    return {
        "status": "success",
        "message": "Successfuly created",
        "data": new_course
    }

# Replace course detail


@app.put("/courses/{id}")
def replace_course(id: int, course: CourseUpdate):
    existing_course = find_course(id)
    if existing_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    existing_course["title"] = course.title.strip().title()
    existing_course["description"] = course.description.strip()
    existing_course["price"] = course.price
    existing_course["duration"] = course.duration
    existing_course["instructor"] = course.instructor
    existing_course["category"] = course.category.strip()
    existing_course["rating"] = course.rating
    existing_course["active"] = course.active

    return {
        "status": "success",
        "message": "Course replaced successfully",
        "data": existing_course
    }

# Update course


@app.patch("/courses/{id}")
def update_course(id: int, course: CourseUpdate):
    existing_course = find_course(id)
    if existing_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = course.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        existing_course[field] = value

    return {
        "status": "success",
        "message": "Course successfully updated",
        "data": existing_course
    }

# Delete course


@app.delete("/courses/{id}")
def delete_course(id: int):
    course = find_course(id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    courses.remove(course)
    return {
        "status": "success",
        "message": "Deleted successfully",
        "data": course
    }
