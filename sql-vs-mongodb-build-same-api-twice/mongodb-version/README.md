# MongoDB Version

FastAPI + PyMongo + MongoDB.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env`:

```env
MONGODB_URL=mongodb+srv://USERNAME:PASSWORD@CLUSTER.mongodb.net/?retryWrites=true&w=majority&appName=taskmanagement
MONGODB_DATABASE=task_management_db
```

Run:

```powershell
uvicorn app.main:app --reload
```

Docs:

http://127.0.0.1:8000/docs

## MongoDB model

Collections:

- `users`
- `projects`
- `tasks`

Task documents keep references to `project_id` and `assigned_to`. MongoDB does not enforce these references as relational foreign keys; the FastAPI application validates them before assignment/creation.
