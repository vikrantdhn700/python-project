from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError

from ..database import users_collection
from ..schemas import UserCreate, UserResponse
from ..utils import serialize_document, utc_now

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate):
    document = {
        "name": data.name,
        "email": data.email,
        "created_at": utc_now(),
    }

    try:
        result = users_collection.insert_one(document)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Email already exists")

    document["_id"] = result.inserted_id
    return serialize_document(document)


@router.get("", response_model=list[UserResponse])
def get_users():
    return [serialize_document(doc) for doc in users_collection.find().sort("_id", 1)]
