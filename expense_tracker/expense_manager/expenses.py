"""Expense management functions for the Expense Tracker application."""

import csv
import os
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

FILE_NAME = log_file_path / "expenses.csv"


def initialize_file():
    """Create CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["id", "date", "category", "description", "amount"]
            )


def load_expenses():
    """Load all expenses from CSV."""
    initialize_file()

    expenses = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        return []

    except OSError as e:
        raise OSError(f"Error reading expense file: {e}") from e

    return expenses


def save_expenses(expenses):
    """Save all expenses to CSV."""

    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "id",
                "date",
                "category",
                "description",
                "amount"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(expenses)

    except OSError as e:
        raise OSError(f"Error saving expenses: {e}") from e


def generate_expense_id(expenses):
    """Generate a new unique expense ID."""

    if not expenses:
        return 1

    ids = [int(expense["id"]) for expense in expenses]

    return max(ids) + 1


def add_expense(date, category, description, amount):
    """Add a new expense."""

    expenses = load_expenses()

    expense_id = generate_expense_id(expenses)

    new_expense = {
        "id": expense_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return new_expense


def delete_expense(expense_id):
    """Delete an expense using its ID."""

    expenses = load_expenses()

    original_count = len(expenses)

    expenses = [
        expense
        for expense in expenses
        if int(expense["id"]) != expense_id
    ]

    if len(expenses) == original_count:
        return False

    save_expenses(expenses)

    return True


def update_expense(
    expense_id,
    date,
    category,
    description,
    amount
):
    """Update an existing expense."""

    expenses = load_expenses()

    for expense in expenses:

        if int(expense["id"]) == expense_id:

            expense["date"] = date
            expense["category"] = category
            expense["description"] = description
            expense["amount"] = amount

            save_expenses(expenses)

            return True

    return False


def get_expense_by_id(expense_id):
    """Find an expense using its ID."""

    expenses = load_expenses()

    for expense in expenses:

        if int(expense["id"]) == expense_id:
            return expense

    return None
