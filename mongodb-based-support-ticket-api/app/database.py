import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "support_ticket_db")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL is missing. Add it to your .env file.")

# One MongoClient is shared by the application.
client = MongoClient(
    MONGODB_URL,
    server_api=ServerApi("1"),
    serverSelectionTimeoutMS=10000,
)

database = client[MONGODB_DATABASE]
tickets_collection = database["tickets"]
