# Customer Support Ticket API — FastAPI + MongoDB

A beginner-friendly REST API for customer support tickets. It uses FastAPI, Pydantic validation, and MongoDB documents.

## Why MongoDB instead of PostgreSQL?

MongoDB is a good fit because a ticket naturally contains nested and variable data. Each ticket stores its customer, tags, and a growing list of comments in one document. This avoids separate comment/tag tables and SQL joins. PostgreSQL would be a better choice when strict relational rules, complex joins, and highly structured reporting are the main needs.

See [mongo_structure.md](mongo_structure.md) for the document design.

## Setup

1. Copy the environment example:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Set `MONGODB_URL` in `.env`. Use a local MongoDB URL or an Atlas connection string. Never commit `.env`.

3. Create a virtual environment and install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. Start the API:

   ```powershell
   python -m uvicorn app.main:app --reload
   ```

5. Open API documentation: <http://127.0.0.1:8000/docs>

## Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| POST | `/tickets` | Create a ticket |
| GET | `/tickets` | List tickets; filter/search them |
| GET | `/tickets/{ticket_id}` | Get one ticket |
| PATCH | `/tickets/{ticket_id}` | Update ticket details/tags |
| PATCH | `/tickets/{ticket_id}/status` | Change ticket status |
| POST | `/tickets/{ticket_id}/comments` | Add a nested comment |
| DELETE | `/tickets/{ticket_id}` | Delete a ticket |

### Filtering and search

```text
GET /tickets?priority=high&status=open
GET /tickets?category=account
GET /tickets?search=password
```

### Create-ticket example

```json
{
  "customer": {
    "name": "Asha Kumar",
    "email": "asha@example.com",
    "phone": "+91-9876543210"
  },
  "title": "Unable to reset password",
  "description": "The reset email link says it has expired.",
  "category": "account",
  "priority": "high",
  "tags": ["login", "password"]
}
```

## GitHub submission

Commit the source code, `requirements.txt`, `.env.example`, this README, and `mongo_structure.md`. `.env` and `.venv` are excluded by `.gitignore`.
