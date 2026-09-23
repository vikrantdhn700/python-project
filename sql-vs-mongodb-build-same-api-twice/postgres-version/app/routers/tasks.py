from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project, Task, User
from app.schemas import AssignTask, TaskCreate, TaskResponse, UpdateStatus

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_task_or_404(task_id: int, db: Session) -> Task:
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    if not db.get(Project, data.project_id):
        raise HTTPException(status_code=404, detail="Project not found")

    task = Task(
        project_id=data.project_id,
        title=data.title,
        description=data.description,
        status="pending",
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("", response_model=list[TaskResponse])
def get_tasks(
    project_id: int | None = Query(default=None),
    status: str | None = Query(default=None),
    assigned_to: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Task)

    if project_id is not None:
        query = query.filter(Task.project_id == project_id)
    if status is not None:
        if status not in {"pending", "in_progress", "completed"}:
            raise HTTPException(status_code=400, detail="Invalid status")
        query = query.filter(Task.status == status)
    if assigned_to is not None:
        query = query.filter(Task.assigned_to == assigned_to)

    return query.order_by(Task.id).all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_or_404(task_id, db)


@router.patch("/{task_id}/assign", response_model=TaskResponse)
def assign_task(task_id: int, data: AssignTask, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    if not db.get(User, data.assigned_to):
        raise HTTPException(status_code=404, detail="User not found")

    task.assigned_to = data.assigned_to
    db.commit()
    db.refresh(task)
    return task


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_status(task_id: int, data: UpdateStatus, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)
    task.status = data.status
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)
    db.delete(task)
    db.commit()
