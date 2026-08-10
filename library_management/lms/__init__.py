""" Library Management System - Initialization Module """

from .books import (
    load_books,
    save_books,
    add_book,
    borrow_book,
    return_book,
    search_book,
    view_available_books,
    view_all_books,
    get_book_by_id
)

from .borrow_history import (
    load_history,
    save_history,
    add_history,
    display_history
)

from .logger import (
    log_message
)

from .validation import (
    validate_book_id,
    validate_title,
    validate_author,
    validate_borrower
)

from .exceptions import (
    LibraryManagementError
)

__all__ = [
    "load_books",
    "save_books",
    "add_book",
    "borrow_book",
    "return_book",
    "search_book",
    "view_available_books",
    "view_all_books",
    "get_book_by_id",

    "load_history",
    "save_history",
    "add_history",
    "display_history",

    "log_message",

    "validate_book_id",
    "validate_title",
    "validate_author",
    "validate_borrower",

    "LibraryManagementError"
]
