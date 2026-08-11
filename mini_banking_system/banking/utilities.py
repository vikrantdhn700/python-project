"""Small reusable formatting and ID helper functions."""

from datetime import datetime
from uuid import uuid4


def generate_transaction_id():
    """Return a short unique transaction ID."""
    return uuid4().hex[:12].upper()


def current_datetime():
    """Return the current local date and time as readable text."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_money(amount):
    """Format a number as currency."""
    return f"${float(amount):,.2f}"
