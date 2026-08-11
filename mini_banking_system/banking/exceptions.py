"""Custom exceptions for expected banking errors."""


class BankingError(Exception):
    """Base exception for all expected banking errors."""


class InsufficientBalanceError(BankingError):
    """Raised when an account cannot cover an operation."""


class InvalidAmountError(BankingError):
    """Raised when a money amount is invalid."""


class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""


class DuplicateAccountError(BankingError):
    """Raised when an account number is already in use."""


class InvalidInputError(BankingError):
    """Raised when text input is empty or incorrectly formatted."""


class SameAccountTransferError(BankingError):
    """Raised when sender and receiver are the same account."""
