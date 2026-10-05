# super30-docker-assignment — All Steps

This document lists step-by-step commands and explanations for Tasks 1–23. Follow each task sequentially.

---

Task 01 — Pull Ubuntu and run interactively

Commands:

```powershell
# Pull latest Ubuntu image
docker pull ubuntu:latest

# Run an interactive container and open bash
docker run --rm -it ubuntu:latest bash
```

Inside the container run at least 5 commands, e.g.:

```sh
ls -la
pwd
whoami
apt-get update
uname -a
```

Purpose: verify you can pull and run images, and execute commands inside containers.

---

Task 02 — Ubuntu + Python installed and run a program

Commands:

```powershell
# Start a container and install python3 interactively
docker run --rm -it ubuntu:latest bash
# inside container
apt-get update && apt-get install -y python3 python3-pip
python3 -c "print('Hello from Python inside container')"
```

Alternative: create and run a one-off container with command:

```powershell
docker run --rm ubuntu:latest bash -c "apt-get update && apt-get install -y python3 && python3 -c \"print('Hello')\""
```

---

Task 03 — Run a container with a custom name

Commands:

```powershell
docker run --rm -it --name super30-linux ubuntu:latest bash
```

Verify name by running `docker ps -a` in another shell.

---

Task 04 — Detached container lifecycle

Commands:

```powershell
# Run detached
docker run -d --name super30-detached nginx:alpine

# Verify running
docker ps

# Stop
docker stop super30-detached

# Restart
docker start super30-detached

# Remove
docker rm -f super30-detached
```

Explain: `-d` runs in background; `docker ps` lists running containers.

---

Task 05 — Pull at least three images and list images

Commands:

```powershell
docker pull ubuntu:latest
docker pull nginx:alpine
docker pull python:3.11-slim

docker images
```

---

Task 06 — Simple Python app and Dockerfile

Files to create:
- `task-06/app.py` — a small script that prints a message or runs a basic HTTP server.
- `task-06/Dockerfile`

Example `app.py`:

```python
print('Hello from super30 python app')
```

Example `Dockerfile`:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/app.py
CMD ["python", "app.py"]
```

Build and run:

```powershell
docker build -t super30-python-app .
docker run --rm super30-python-app
```

---

Task 07 — Build image named `super30-python-app` and run it

Commands (from `task-06` folder):

```powershell
docker build -t super30-python-app .
docker run --rm super30-python-app
```

Verify program output appears in container logs/STDOUT.

---

Task 08 — Create FastAPI app and containerize

Files:
- `task-08/app/main.py`
- `task-08/requirements.txt` (fastapi, uvicorn)
- `task-08/Dockerfile`

Quick `main.py`:

```python
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello FastAPI'}
```

`requirements.txt`:

```
fastapi
uvicorn[standard]
```

`Dockerfile`:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```powershell
docker build -t super30-api .
docker run --rm -p 8000:8000 super30-api
```

---

Task 09 — Run FastAPI on port 8000 and verify

Commands to run locally:

```powershell
docker run --rm -p 8000:8000 super30-api
# Then visit http://localhost:8000/ in your browser or curl
curl http://localhost:8000/
```

---

Task 10 — Map host port 5000 to container 8000

Commands:

```powershell
docker run --rm -p 5000:8000 super30-api
```

Explanation: Docker's `-p HOST:CONTAINER` publishes container port 8000 on host port 5000 — incoming requests to host:5000 are forwarded to container:8000.

---

Task 11 — Dockerfile using WORKDIR, COPY, RUN, EXPOSE, CMD

Example `Dockerfile` and purpose of each instruction:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app            # sets working directory inside image
COPY requirements.txt ./ # copies files from build context
RUN pip install -r requirements.txt # runs command at build time to install deps
COPY . /app             # copy app files into container
EXPOSE 8000             # documents container listens on this port (informational)
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"] # default runtime command
```

- `WORKDIR`: set working directory for following commands and at runtime.
- `COPY`: copy files from build context into image.
- `RUN`: execute commands during image build; results are committed to image layers.
- `EXPOSE`: metadata describing that container listens on specified ports.
- `CMD`: default command executed when container starts (overridable).

---

Task 12 — `requirements.txt` with FastAPI and Uvicorn and install during build

`requirements.txt` example:

```
fastapi==0.99.0
uvicorn[standard]==0.23.0
psycopg2-binary==2.9.6  # if using PostgreSQL later
```

`Dockerfile` should use `RUN pip install -r requirements.txt` as shown above to install dependencies during build.

---

Task 13 — Pass an environment variable to a container

Commands & example:

```powershell
docker run --rm -e GREETING=super30 -p 8000:8000 super30-api
```

In FastAPI `main.py` read it with `import os; os.getenv('GREETING')` and return it in an endpoint.

---

Task 14 — Use a `.env` file and do not commit sensitive values

Create `.env`:

```
DB_USER=super30
DB_PASS=change-me
SECRET_KEY=local-dev
```

Run with docker-compose or `--env-file`:

```powershell
docker run --rm --env-file .env -p 8000:8000 super30-api
```

Add `.env` to `.gitignore` and never commit secrets.

---

Task 15 — Docker volume persistence across containers

Commands:

```powershell
# create volume
docker volume create super30-data

# start a temporary container and write a file into the volume
docker run --rm -v super30-data:/data --name writer alpine sh -c "echo hello > /data/greeting.txt"

# start another container using the same volume and read the file
docker run --rm -v super30-data:/data alpine cat /data/greeting.txt
```

Proves data persists beyond container removal.

---

Task 16 — Two containers on custom network communicate

Commands:

```powershell
# create network
docker network create super30-net

# run a simple HTTP server container (python) attached to the network
docker run -d --name service-a --network super30-net python:3.11-slim sh -c "python -m http.server 9000"

# run an interactive container on same network and curl the service
docker run --rm --network super30-net curlimages/curl curl http://service-a:9000
```

Service names resolve via Docker DNS on the custom network.

---

Task 17 — PostgreSQL container with env-configured DB

Commands:

```powershell
docker run -d --name super30-postgres -e POSTGRES_DB=super30db -e POSTGRES_USER=super30 -e POSTGRES_PASSWORD=super30pass -v super30-pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:15-alpine
```

Verify with `docker logs super30-postgres` and by connecting with `psql` or a DB client.

---

Task 18 — FastAPI app connects to PostgreSQL in separate container

Steps:
- Update FastAPI to use `asyncpg` or `psycopg2` and read DB connection from env vars (host, port, user, pass, db).
- Ensure both containers share a Docker network or use docker-compose.

Example connection string:

```
postgresql://super30:super30pass@super30-postgres:5432/super30db
```

Test by running the FastAPI container on the same network and hitting an endpoint that queries the DB.

---

Task 19 — `docker-compose.yml` for FastAPI + PostgreSQL

Example `docker-compose.yml`:

```yaml
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: super30db
      POSTGRES_USER: super30
      POSTGRES_PASSWORD: super30pass
    volumes:
      - super30-pgdata:/var/lib/postgresql/data
  api:
    build: ./task-08
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://super30:super30pass@db:5432/super30db
    ports:
      - "8000:8000"
volumes:
  super30-pgdata: {}
```

Start with:

```powershell
docker compose up --build
```

---

Task 20 — Add Frontend service

Approach:
- Create a simple frontend (static HTML/JS) served by `nginx` or `http-server`.
- Add a `frontend` service in `docker-compose.yml` that builds or serves the static files and communicates with `api` via network.

Compose snippet:

```yaml
  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - api
```

---

Task 21 — Implement `/health` and Docker healthcheck

FastAPI `main.py` add:

```python
@app.get('/health')
def health():
    return {'status':'ok'}
```

Add `healthcheck` to `docker-compose.yml` for `api`:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

`depends_on` supports `condition: service_healthy` on older compose; with v2+ use startup ordering carefully.

---

Task 22 — CRUD FastAPI + PostgreSQL + Compose with persistence

Requirements:
- Implement endpoints: POST `/students`, GET `/students/{id}`, PUT `/students/{id}`, DELETE `/students/{id}`
- Use SQLAlchemy or async equivalents; store data in Postgres.
- Ensure DB volume is defined in compose so data survives restarts.

Example flow:

```powershell
docker compose up --build
# create student via curl
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{"name":"Alice","age":20}'
# restart services
docker compose down && docker compose up -d
# verify student still exists
curl http://localhost:8000/students
```

---

Task 23 — Final Student Management System (full project)

Structure:

- `frontend/` — simple UI (HTML/JS) calling backend APIs
- `api/` — FastAPI service with CRUD endpoints, DB models, migrations optional
- `db/` — Postgres service using persistent volume
- `docker-compose.yml` — builds and starts all services
- `.env` — environment variables (not committed)

Key requirements:
- Command to start everything: `docker compose up --build`
- Provide sample requests and UI usage in README
- Ensure DB volume persists and networking allows frontend→api communication

---

Deliverables

- Directory `task-01` through `task-23` with code, Dockerfiles, and READMEs
- Root `README.md` with overall instructions
- `ALL_STEPS.md` (this file)
- `generate_docx.py` — script to convert `ALL_STEPS.md` to `ALL_STEPS.docx`

---

How to generate the `.docx` file locally

1. Install Python and pip.
2. Install dependency:

```powershell
pip install python-docx
```

3. Run the script:

```powershell
python generate_docx.py ALL_STEPS.md ALL_STEPS.docx
```

This will produce `ALL_STEPS.docx` with the same content as this file.

---

Notes

- Add `.env` to `.gitignore` to avoid committing secrets.
- Use `docker compose` (v2) where possible for multi-service orchestration.
