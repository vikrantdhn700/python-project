"""Validation functions shared by customer and transaction modules."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from .exceptions import InvalidAmountError, InvalidInputError


def validate_account_number(account_number):
    """Validate and normalize an account number."""
    account_number = str(account_number).strip().upper()
    if not account_number:
        raise InvalidInputError("Account number cannot be empty.")
    if not account_number.isalnum():
        raise InvalidInputError(
            "Account number must contain only letters and numbers.")
    return account_number


def validate_name(name):
    """Validate and clean a customer name."""
    name = str(name).strip()
    if not name:
        raise InvalidInputError("Customer name cannot be empty.")
    return name


def _to_money(value, message):
    """Convert input to a Decimal with two decimal places."""
    try:
        amount = Decimal(str(value)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError) as e:
        raise InvalidAmountError(f"{message}: {e}") from e
    if not amount.is_finite():
        raise InvalidAmountError(message)
    return amount


def validate_amount(amount):
    """Return a numeric transaction amount greater than zero."""
    amount = _to_money(amount, "Amount must be numeric.")
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")
    return amount


def validate_initial_balance(amount):
    """Return a numeric initial balance that is not negative."""
    amount = _to_money(amount, "Initial balance must be numeric.")
    if amount < 0:
        raise InvalidAmountError("Initial balance cannot be negative.")
    return amount
