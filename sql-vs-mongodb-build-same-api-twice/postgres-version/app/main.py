from fastapi import FastAPI

from app.database import Base, engine
from app.routers import projects, tasks, users

app = FastAPI(
    title="Task/Project Management API - PostgreSQL",
    version="1.0.0",
    description="FastAPI + Neon PostgreSQL implementation",
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Task/Project Management API",
        "database": "PostgreSQL",
        "docs": "/docs",
    }
