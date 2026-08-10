""" Validators for the payroll application."""

from .exceptions import (
    InvalidInputError,
    InvalidSalaryError,
    InvalidBonusError,
)


def validate_employee_id(employee_id):
    """Validate employee ID."""

    employee_id = str(employee_id).strip()

    if not employee_id:
        raise InvalidInputError(
            "Employee ID cannot be empty."
        )

    return employee_id


def validate_name(name):
    """Validate employee name."""

    name = str(name).strip()

    if not name:
        raise InvalidInputError(
            "Employee name cannot be empty."
        )

    return name


def validate_department(department):
    """Validate department."""

    department = str(department).strip()

    if not department:
        raise InvalidInputError(
            "Department cannot be empty."
        )

    return department


def validate_salary(salary):
    """Validate salary."""

    try:
        salary = float(salary)

    except (ValueError, TypeError) as error:

        raise InvalidSalaryError(
            f"Salary must be a valid number. {error}") from error

    if salary <= 0:

        raise InvalidSalaryError("Salary must be greater than zero.")

    return round(salary, 2)


def validate_bonus_percentage(bonus):
    """Validate bonus percentage."""

    try:
        bonus = float(bonus)

    except (ValueError, TypeError) as error:

        raise InvalidBonusError(
            f"Bonus percentage must be a valid number. {error}"
        ) from error

    if bonus < 0 or bonus > 100:

        raise InvalidBonusError(
            "Bonus percentage must be between 0 and 100."
        )

    return round(bonus, 2)


def validate_month(month):
    """Validate payroll month."""

    month = str(month).strip()

    if not month:

        raise InvalidInputError(
            "Payroll month cannot be empty."
        )

    return month
