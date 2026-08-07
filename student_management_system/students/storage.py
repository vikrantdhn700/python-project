import json
import os
from pathlib import Path
from .exceptions import StudentException

script_path = Path(__file__).resolve().parent.parent

STORAGE_FILE = script_path/"students.json"

def load_data():
    if not os.path.exists(STORAGE_FILE):
        return {}

    try:
        if STORAGE_FILE.stat().st_size == 0:
            return {}

        with open(STORAGE_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as err:
        raise StudentException(f"Failed to read data file: {str(err)}")

def save_students(data):
    try:
        with open(STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as err:
        raise StudentException(f"Failed to write data file: {str(err)}")