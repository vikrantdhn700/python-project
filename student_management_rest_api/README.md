# Student Management API

A simple **Student Management System** built with **FastAPI** and **Pydantic**.

The application demonstrates REST API concepts such as:

- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Path parameters
- Request bodies
- Pydantic validation
- HTTP status codes
- Error handling
- CRUD operations
- In-memory data storage using a Python list

> **Note:** Student data is currently stored in a Python list. Data will be lost when the application restarts.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
student-management/
│
├── main.py
└── README.md
```

## Installation

Create and activate a virtual environment if required:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install fastapi uvicorn
```

## Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Initial Student Data

The application starts with three students:

| ID | Name | Age | Course |
|---:|---|---:|---|
| 1 | Rahul | 20 | Python |
| 2 | Priya | 21 | Data Science |
| 3 | Amit | 22 | FastAPI |

## Pydantic Validation

### StudentCreate

Used when creating a student with `POST /students`.

```python
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=10, le=100)
    course: str = Field(min_length=2, max_length=100)
```

Validation rules:

- `name` must be a string with 2–50 characters.
- `age` must be an integer between 10 and 100.
- `course` must be a string with 2–100 characters.

### StudentUpdate

Used for PUT and PATCH requests.

```python
class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    course: Optional[str]
```

For PATCH, only fields included in the request are updated.

## API Endpoints

### 1. Get All Students

```http
GET /students
```

Returns all students.

**Success response: `200 OK`**

Example:

```json
{
    "status": "success",
    "message": "Students found",
    "data": [
        {
            "id": 1,
            "name": "Rahul",
            "age": 20,
            "course": "Python"
        }
    ]
}
```

If the student list is empty, the API returns:

```text
404 Not Found
```

---

### 2. Get Student by ID

```http
GET /students/{id}
```

Example:

```http
GET /students/1
```

**Success response: `200 OK`**

```json
{
    "status": "success",
    "message": "Student found",
    "data": {
        "id": 1,
        "name": "Rahul",
        "age": 20,
        "course": "Python"
    }
}
```

If the ID does not exist:

```text
404 Not Found
```

Response:

```json
{
    "detail": "Student not found"
}
```

---

### 3. Create Student

```http
POST /students
```

Request body:

```json
{
    "name": "Vikash",
    "age": 23,
    "course": "Python"
}
```

**Success response: `201 Created`**

```json
{
    "status": "success",
    "message": "Student created successfully",
    "data": {
        "id": 4,
        "name": "Vikash",
        "age": 23,
        "course": "Python"
    }
}
```

The application automatically generates the student ID.

#### Invalid request example

```json
{
    "name": "A",
    "age": 5,
    "course": "Python"
}
```

Pydantic validation rejects invalid values.

FastAPI normally returns:

```text
422 Unprocessable Entity
```

---

### 4. Replace Student

```http
PUT /students/{id}
```

Example:

```http
PUT /students/1
```

Request body:

```json
{
    "name": "Rahul Sharma",
    "age": 25,
    "course": "Python"
}
```

The existing student's fields are replaced.

**Success response: `200 OK`**

```json
{
    "status": "success",
    "message": "Student successfully replace",
    "data": {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 25,
        "course": "Python"
    }
}
```

If the ID does not exist:

```text
404 Not Found
```

---

### 5. Partially Update Student

```http
PATCH /students/{id}
```

Example:

```http
PATCH /students/1
```

Request body:

```json
{
    "age": 26
}
```

Only the `age` field is updated.

The code uses:

```python
update_data = student.model_dump(exclude_unset=True)
```

This ensures that fields not included in the request are not overwritten.

**Success response: `200 OK`**

```json
{
    "status": "success",
    "message": "Student successfully updated",
    "data": {
        "id": 1,
        "name": "Rahul",
        "age": 26,
        "course": "Python"
    }
}
```

---

### 6. Delete Student

```http
DELETE /students/{id}
```

Example:

```http
DELETE /students/1
```

The student is removed from the in-memory list.

**Success response: `200 OK`**

```json
{
    "status": "success",
    "message": "Student deleted successfully",
    "data": {
        "id": 1,
        "name": "Rahul",
        "age": 20,
        "course": "Python"
    }
}
```

If the ID does not exist:

```text
404 Not Found
```

## HTTP Methods Summary

| Method | Endpoint | Purpose | Success |
|---|---|---|---|
| GET | `/students` | Get all students | 200 |
| GET | `/students/{id}` | Get one student | 200 |
| POST | `/students` | Create student | 201 |
| PUT | `/students/{id}` | Replace student | 200 |
| PATCH | `/students/{id}` | Partially update student | 200 |
| DELETE | `/students/{id}` | Delete student | 200 |

## Status Codes

| Status Code | Meaning | Example |
|---:|---|---|
| 200 | OK | Successful GET, PUT, PATCH, DELETE |
| 201 | Created | Student successfully created |
| 404 | Not Found | Student ID does not exist |
| 422 | Unprocessable Entity | Pydantic validation failure |

## Error Handling

The application uses FastAPI's `HTTPException` for application-level errors.

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

Invalid request data is automatically validated by Pydantic/FastAPI.

For example, if `age` is outside the allowed range, FastAPI returns a validation error.

## CRUD Operations

This project implements the complete CRUD pattern:

```text
Create  → POST
Read    → GET
Update  → PUT / PATCH
Delete  → DELETE
```

## Testing

The easiest way to test the APIs is through the automatically generated Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can also test the APIs using Postman, Thunder Client, or another REST API client.

## Learning Objectives

This project is designed to practice:

1. Creating FastAPI routes.
2. Understanding HTTP methods.
3. Working with path parameters.
4. Sending JSON request bodies.
5. Using Pydantic models for validation.
6. Understanding PUT vs PATCH.
7. Returning appropriate HTTP status codes.
8. Handling invalid student IDs.
9. Performing CRUD operations.
10. Working with temporary in-memory data before introducing a database.

## Future Improvements

Possible next steps:

- Add PostgreSQL or Supabase database storage.
- Add separate service and router files.
- Add authentication and authorization.
- Add pagination and query parameters.
- Add search and filtering.
- Add automated tests with `pytest`.
- Add database validation and constraints.
- Add logging.
- Add Docker support.

## Author

Student Management API — FastAPI learning project.
