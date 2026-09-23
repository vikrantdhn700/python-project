from datetime import datetime, timezone

from bson import ObjectId
from fastapi import HTTPException


def parse_object_id(value: str) -> ObjectId:
    if not ObjectId.is_valid(value):
        raise HTTPException(status_code=400, detail="Invalid ID")
    return ObjectId(value)


def serialize_document(document: dict) -> dict:
    result = dict(document)
    result["id"] = str(result.pop("_id"))
    for key in ("project_id", "assigned_to"):
        if result.get(key) is not None and isinstance(result[key], ObjectId):
            result[key] = str(result[key])
    return result


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
