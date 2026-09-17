# Course Management Backend API

A simple Course Management Backend built with FastAPI and Pydantic.

## Features
- Get all courses
- Filter by category, price range, and active status
- Get a course by ID
- Create, replace, partially update, and delete courses
- Pydantic validation
- HTTP error handling

## Technologies
- Python
- FastAPI
- Pydantic
- Uvicorn
- In-memory Python list

## Installation
```bash
pip install fastapi uvicorn
```

## Run
```bash
uvicorn main:app --reload
```

- API: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Course Fields
| Field | Type | Validation |
|---|---|---|
| `id` | int | Unique course ID |
| `title` | str | 2–100 characters |
| `description` | str | 2–500 characters |
| `price` | float | >= 0 |
| `duration` | int | > 0 |
| `instructor` | str | 2–100 characters |
| `category` | str | 2–50 characters |
| `rating` | float | 0–5 |
| `active` | bool | Defaults to true |

## API Endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/courses/` | Get/filter courses |
| GET | `/courses/{id}` | Get one course |
| POST | `/courses/` | Create course |
| PUT | `/courses/{id}` | Replace course |
| PATCH | `/courses/{id}` | Partially update course |
| DELETE | `/courses/{id}` | Delete course |

## Get Courses
```http
GET /courses/
```

### Filters
```http
GET /courses/?category=python
GET /courses/?min_price=1000
GET /courses/?max_price=3000
GET /courses/?min_price=500&max_price=3000
GET /courses/?active=true
GET /courses/?active=false
GET /courses/?category=python&min_price=500&max_price=5000&active=true
```

Category matching is case-insensitive. If `min_price > max_price`, the API returns `400`.

## Get Course by ID
```http
GET /courses/1
```

If the course does not exist, the API returns `404` with `Course not found`.

## Create Course
```http
POST /courses/
```

Example body:
```json
{
  "title": "Python FastAPI Masterclass",
  "description": "Learn how to build APIs using Python and FastAPI.",
  "price": 3000,
  "duration": 40,
  "instructor": "Rahul Sharma",
  "category": "python",
  "rating": 4.7,
  "active": true
}
```

The API generates the next course ID automatically.

## Replace Course
```http
PUT /courses/1
```

The current implementation uses `CourseUpdate`; for strict full replacement, a model with all required fields would normally be used.

## Partially Update Course
```http
PATCH /courses/1
```

Example:
```json
{
  "price": 1200,
  "rating": 4.6
}
```

The implementation uses:
```python
course.model_dump(exclude_unset=True)
```
so only supplied fields are changed.

## Delete Course
```http
DELETE /courses/4
```

The course is removed from the in-memory list. Missing courses return `404`.

## Response Format
```json
{
  "status": "success",
  "message": "Courses successfully fetched",
  "data": [
    {
      "id": 1,
      "title": "Python for Beginners",
      "description": "Learn Python programming from basics.",
      "price": 999,
      "duration": 30,
      "instructor": "Rahul Sharma",
      "category": "python",
      "rating": 4.5,
      "active": true
    }
  ]
}
```

## Status Codes
| Code | Meaning |
|---|---|
| `200` | Successful request |
| `400` | Invalid price range |
| `404` | Course not found |
| `422` | FastAPI/Pydantic validation error |

## Validation Examples
- Rating greater than `5` is rejected.
- Duration `0` is rejected.
- Title shorter than 2 characters is rejected.

## In-Memory Storage
Courses are stored in a Python list. Data is not persistent and changes are lost when the application restarts.

## Testing
Open Swagger at `http://127.0.0.1:8000/docs` and test the CRUD and filtering endpoints. Also test invalid IDs, invalid request data, `active=true/false`, and invalid price ranges.

## Learning Objectives
- FastAPI application setup
- REST API methods
- Path and query parameters
- Request bodies
- Pydantic models and validation
- Response models
- HTTP status codes and `HTTPException`
- CRUD operations
- Filtering
- `model_dump(exclude_unset=True)`
- Swagger documentation

## Future Improvements
- PostgreSQL database
- SQLAlchemy
- Authentication/authorization
- Pagination and sorting
- Course search
- pytest automated tests
- Logging
- Environment variables
- Docker
