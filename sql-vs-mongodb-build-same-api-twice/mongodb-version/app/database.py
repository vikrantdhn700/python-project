import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "task_management_db")

if not MONGODB_URL:
    raise RuntimeError("MONGODB_URL is not configured in .env")

client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=10000)
database = client[MONGODB_DATABASE]

users_collection = database["users"]
projects_collection = database["projects"]
tasks_collection = database["tasks"]

# Helpful indexes for filtering.
tasks_collection.create_index("project_id")
tasks_collection.create_index("status")
tasks_collection.create_index("assigned_to")
users_collection.create_index("email", unique=True)
