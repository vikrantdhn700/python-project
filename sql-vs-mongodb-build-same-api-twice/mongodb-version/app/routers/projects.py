from fastapi import APIRouter, HTTPException, status

from ..database import projects_collection
from ..schemas import ProjectCreate, ProjectResponse
from ..utils import parse_object_id, serialize_document, utc_now

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(data: ProjectCreate):
    document = {
        "name": data.name,
        "description": data.description,
        "created_at": utc_now(),
    }
    result = projects_collection.insert_one(document)
    document["_id"] = result.inserted_id
    return serialize_document(document)


@router.get("", response_model=list[ProjectResponse])
def get_projects():
    return [
        serialize_document(doc)
        for doc in projects_collection.find().sort("_id", 1)
    ]


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: str):
    document = projects_collection.find_one({"_id": parse_object_id(project_id)})
    if not document:
        raise HTTPException(status_code=404, detail="Project not found")
    return serialize_document(document)
