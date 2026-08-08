"""Validation functions."""

from datetime import datetime


def validate_date(date):
    """Validate date format YYYY-MM-DD."""

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError as e:
        raise ValueError(
            f"Invalid date. Use YYYY-MM-DD format. {e}"
        ) from e


def validate_amount(amount):
    """Validate expense amount."""

    try:
        amount = float(amount)

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        return amount

    except ValueError as e:
        raise ValueError(
            f"Invalid amount. Please enter a positive number. {e}"
        ) from e


def validate_category(category):
    """Validate expense category."""

    if not category.strip():
        raise ValueError(
            "Category cannot be empty."
        )

    return category.strip()


def validate_description(description):
    """Validate expense description."""

    if not description.strip():
        raise ValueError(
            "Description cannot be empty."
        )

    return description.strip()


def validate_expense_id(expense_id):
    """Validate expense ID."""

    try:
        expense_id = int(expense_id)

        if expense_id <= 0:
            raise ValueError(
                f"Expense ID must be greater than zero. {expense_id}"
            )

        return expense_id

    except ValueError as e:
        raise ValueError(
            f"Expense ID must be a valid number. {e}"
        ) from e


def validate_month(month):
    """Validate month in YYYY-MM format."""

    try:
        datetime.strptime(month, "%Y-%m")
        return True

    except ValueError as e:
        raise ValueError(
            f"Invalid month. Use YYYY-MM format. {e}"
        ) from e
