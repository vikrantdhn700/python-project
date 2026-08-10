"""Borrowing history functions for the library management system."""

import json
import os
from datetime import datetime
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent
HISTORY_FILE = log_file_path / "borrowing_history.json"


def load_history():
    """Load borrowing history from the JSON file."""

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    """Save borrowing history to the JSON file."""

    try:
        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                history,
                file,
                indent=4
            )

    except OSError as error:
        print(f"Unable to save history: {error}")


def add_history(book_id, title, borrower, action):
    """Add a borrow or return event to history."""

    history = load_history()

    record = {
        "book_id": book_id,
        "title": title,
        "borrower": borrower,
        "action": action,
        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    history.append(record)

    save_history(history)


def display_history():
    """Display all borrowing history."""

    history = load_history()

    if not history:
        print("\nNo borrowing history found.")
        return

    print("\n" + "=" * 80)
    print("BORROWING HISTORY")
    print("=" * 80)

    for record in history:
        print(
            f"Date     : {record['date']}"
        )
        print(
            f"Action   : {record['action']}"
        )
        print(
            f"Book ID  : {record['book_id']}"
        )
        print(
            f"Title    : {record['title']}"
        )
        print(
            f"Borrower : {record['borrower']}"
        )
        print("-" * 80)
