# Task / Project Management API — SQL vs NoSQL

This project implements the same Task/Project Management API twice:

- **Version A:** FastAPI + PostgreSQL (designed for Neon)
- **Version B:** FastAPI + MongoDB

The goal is to compare SQL and NoSQL using actual working code.

## Features

Both versions support:

- Create project
- List/get projects
- Create task
- Retrieve tasks
- Filter tasks by project, status, and assignee
- Assign task
- Update task status
- Delete task
- Basic validation
- Swagger/OpenAPI documentation

## Project structure

```text
task-project-management-api/
├── postgres-version/
└── mongodb-version/
```

## Run PostgreSQL version

```powershell
cd postgres-version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put your Neon PostgreSQL URL in `DATABASE_URL`.

Run:

```powershell
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Run MongoDB version

```powershell
cd mongodb-version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put your MongoDB connection string in `MONGODB_URL`.

Run:

```powershell
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

## PostgreSQL vs MongoDB

| Area | PostgreSQL | MongoDB |
|---|---|---|
| Model | Relational | Document |
| Storage | Tables/rows | Collections/documents |
| Schema | Structured | Flexible |
| Relationships | Foreign keys | References/application logic |
| Queries | SQL/SQLAlchemy | MongoDB query API |
| Normalization | Common | Depends on document design |
| Transactions | Strong relational transactions | Supports transactions |
| Validation | DB constraints + Pydantic | Pydantic/application validation |
| Flexible fields | JSONB available | Native document flexibility |
| Development | Excellent for structured relationships | Excellent for document-oriented data |

## Actual code comparison

### PostgreSQL query

```python
query = db.query(Task)

if status:
    query = query.filter(Task.status == status)

tasks = query.all()
```

### MongoDB query

```python
query = {}

if status:
    query["status"] = status

tasks = list(tasks_collection.find(query))
```

## Production conclusion

For this particular application, PostgreSQL is a strong production choice because projects, tasks, and users have clear relationships and task assignment benefits from referential integrity and transactional behavior.

MongoDB is also a valid option when task/project documents become more variable or the application's access patterns are primarily document-oriented.

The choice should be based on the application's data model, consistency requirements, query patterns, and operational needs—not on a blanket rule that SQL or NoSQL is always better.

## Important security note

Never commit `.env` files containing database credentials. Both implementations include `.env` in `.gitignore`.

## Suggested test flow

1. Create a user.
2. Create a project.
3. Create a task for that project.
4. Assign the task to the user.
5. Change the task status.
6. Filter tasks by status/project/assignee.
7. Delete the task.
8. Restart the API and verify PostgreSQL data remains available.
