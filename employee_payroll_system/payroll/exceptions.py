"""Custom exceptions for the payroll application."""


class PayrollError(Exception):
    """Base exception for payroll-related errors."""


class InvalidInputError(PayrollError):
    """Raised when user input is invalid."""


class InvalidSalaryError(PayrollError):
    """Raised when salary is invalid."""


class InvalidBonusError(PayrollError):
    """Raised when bonus percentage is invalid."""


class EmployeeNotFoundError(PayrollError):
    """Raised when an employee does not exist."""


class DuplicateEmployeeError(PayrollError):
    """Raised when an employee ID already exists."""
