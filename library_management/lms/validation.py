""" Validation module for the library management system.
This module provides functions to validate various inputs related to books and borrowers."""

from .exceptions import LibraryManagementError


def validate_book_id(book_id):
    """
    Validate book ID.

    Book ID must be a positive integer.
    """

    try:
        book_id = int(book_id)
    except (ValueError, TypeError) as e:
        raise LibraryManagementError(
            f"Book ID must be a valid integer. {e}") from e

    if book_id <= 0:
        raise LibraryManagementError("Book ID must be greater than 0.")

    return book_id


def validate_title(title):
    """Validate book title."""

    if not title or not title.strip():
        raise LibraryManagementError("Book title cannot be empty.")

    return title.strip()


def validate_author(author):
    """Validate book author."""

    if not author or not author.strip():
        raise LibraryManagementError("Author name cannot be empty.")

    return author.strip()


def validate_borrower(borrower):
    """Validate borrower name."""

    if not borrower or not borrower.strip():
        raise LibraryManagementError("Borrower name cannot be empty.")

    return borrower.strip()
