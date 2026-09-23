# PostgreSQL Version

FastAPI + SQLAlchemy + Neon PostgreSQL.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure:

```env
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@HOST/DATABASE?sslmode=require
```

Run:

```powershell
uvicorn app.main:app --reload
```

Docs:

http://127.0.0.1:8000/docs

## Database

The application can create the tables from the SQLAlchemy models on startup. `schema.sql` is also included for learning and inspection.

For a Neon database, make sure the connection string is correct and SSL is enabled.
