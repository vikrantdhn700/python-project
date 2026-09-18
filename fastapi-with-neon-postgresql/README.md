# Student Course Enrollment API

A FastAPI project connected to Neon PostgreSQL with SQLAlchemy. It manages students, courses, and course enrollments.

## Project structure

```text
app/
  database.py    # Neon database connection
  models.py      # SQLAlchemy table models
  schemas.py     # Pydantic validation and response models
  main.py        # FastAPI routes
.env             # Private Neon connection string
requirements.txt # Python packages
```

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install packages:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Neon connection string:

   ```env
   DATABASE_URL=postgresql+psycopg://USER:PASSWORD@YOUR_NEON_HOST/DATABASE?sslmode=require
   ```

   Do not commit `.env`. It contains your database password and is ignored by Git.

4. Run the API:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
   ```

5. Open the interactive API documentation:

   ```text
   http://127.0.0.1:8000/docs
   ```

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/students/` | Get all students |
| GET | `/students/{id}` | Get one student |
| POST | `/students/` | Create a student |
| PUT/PATCH | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |
| GET | `/courses/` | Get all courses |
| GET | `/courses/{id}` | Get one course |
| POST | `/courses/` | Create a course |
| PUT/PATCH | `/courses/{id}` | Update a course |
| DELETE | `/courses/{id}` | Delete a course |
| GET | `/enrollments/` | Get enrollments with student name and course title |
| POST | `/enrollments/` | Enroll a student in a course |
| DELETE | `/enrollments/{id}` | Delete an enrollment |

## Example course request

```json
{
  "code": "PY-101",
  "title": "Python Basics",
  "description": "Introduction to Python",
  "credit_hours": 6,
  "price": 20000.00
}
```

## Important notes

- Student email addresses must be unique.
- Course codes must be unique.
- A student cannot be enrolled in the same course twice.
- Enrollment data remains in Neon PostgreSQL after restarting the API server.
