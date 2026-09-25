from fastapi import FastAPI

from .routers import projects, tasks, users

app = FastAPI(
    title="Task/Project Management API - MongoDB",
    version="1.0.0",
    description="FastAPI + MongoDB implementation",
)

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
