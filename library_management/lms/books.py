""" Library Management System - Book Management"""
import json
import os
from pathlib import Path

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
from .borrow_history import (
    add_history
)

log_file_path = Path(__file__).resolve().parent.parent


BOOK_FILE = log_file_path / "books.json"


def load_books():
    """Load books from JSON file."""

    if not os.path.exists(BOOK_FILE):
        return []

    try:
        with open(BOOK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        log_message("books.json contains invalid JSON.", "error")
        return []

    except OSError as error:
        log_message(f"Unable to read books file: {error}", "error")
        return []


def save_books(books):
    """Save books to JSON file."""

    try:
        with open(BOOK_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)

    except OSError as error:
        log_message(f"Unable to save books: {error}", "error")
        print("Error: Unable to save books.")


def get_book_by_id(books, book_id):
    """Find a book by ID."""

    book_id = validate_book_id(book_id)

    for book in books:
        if book["id"] == book_id:
            return book

    raise LibraryManagementError(
        f"Book with ID {book_id} was not found."
    )


def add_book(books, title, author):
    """Add a new book."""

    title = validate_title(title)
    author = validate_author(author)

    if books:
        new_id = max(book["id"] for book in books) + 1
    else:
        new_id = 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "available": True,
        "borrower": None
    }

    books.append(book)
    save_books(books)

    log_message(
        f"BOOK ADDED | ID: {new_id} | Title: {title} | Author: {author}",
        "info"
    )

    print("\nBook added successfully.")
    print(f"Book ID: {new_id}")


def borrow_book(books, book_id, borrower):
    """Borrow a book."""

    borrower = validate_borrower(borrower)

    book = get_book_by_id(books, book_id)

    if not book["available"]:
        raise LibraryManagementError(
            f"'{book['title']}' is already borrowed."
        )

    book["available"] = False
    book["borrower"] = borrower

    save_books(books)

    add_history(
        book["id"],
        book["title"],
        borrower,
        "BORROW"
    )

    log_message(
        f"BOOK BORROWED | ID: {book['id']} | Title: {book['title']} | Borrower: {borrower}",
        "info"
    )

    print(
        f"\nBook '{book['title']}' borrowed successfully "
        f"by {borrower}."
    )


def return_book(books, book_id):
    """Return a borrowed book."""

    book = get_book_by_id(books, book_id)

    if book["available"]:
        raise ValueError(
            f"'{book['title']}' is already available."
        )

    borrower = book["borrower"]

    book["available"] = True
    book["borrower"] = None

    save_books(books)

    add_history(
        book["id"],
        book["title"],
        borrower,
        "RETURN"
    )

    log_message(
        f"BOOK RETURNED | ID: {book['id']} | Title: {book['title']} | Borrower: {borrower}",
        "info"
    )

    print(
        f"\nBook '{book['title']}' returned successfully."
    )


def search_book(books, keyword):
    """Search books by ID, title, or author."""

    keyword = keyword.strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []

    for book in books:

        if (
            keyword in str(book["id"])
            or keyword in book["title"].lower()
            or keyword in book["author"].lower()
        ):
            results.append(book)

    if not results:
        print("\nNo books found.")
        return

    print("\nSearch Results")
    print("-" * 70)

    for book in results:
        status = "Available" if book["available"] else "Borrowed"

        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {status}"
        )


def view_available_books(books):
    """Display all available books."""

    available_books = [
        book for book in books
        if book["available"]
    ]

    if not available_books:
        print("\nNo books are currently available.")
        return

    print("\nAvailable Books")
    print("-" * 70)

    for book in available_books:
        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']}"
        )


def view_all_books(books):
    """Display all books."""

    if not books:
        print("\nNo books available in library.")
        return

    print("\nAll Books")
    print("-" * 70)

    for book in books:

        if book["available"]:
            status = "Available"
        else:
            status = f"Borrowed by {book['borrower']}"

        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {status}"
        )
