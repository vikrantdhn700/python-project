# Library Management System

A **console-based Library Management System** built with Python. The application demonstrates package organization, function-based programming, custom exception handling, logging, JSON data persistence, and borrowing history.

## Features

- Add a book
- Borrow a book
- Return a book
- Search books by ID, title, or author
- View available books
- View all books
- View borrowing history
- Persistent book data using JSON
- Persistent borrowing history using JSON
- Custom exception handling
- Logging of borrow and return operations
- Validation of book IDs and input values
- Intentional invalid scenarios to demonstrate exception handling
- Organized using a custom `lms` Python package
- Function-based implementation without OOP

## Project Structure

```text
library_management_system/
│
├── main.py
├── books.json
├── borrowing_history.json
├── library.log
│
└── lms/
    ├── __init__.py
    ├── books.py
    ├── exceptions.py
    ├── borrow_history.py
    ├── logger.py
    └── validation.py
```

## Modules

### `main.py`

The main entry point of the application.

Responsibilities:

- Display the menu
- Accept user input
- Call library functions
- Handle exceptions
- Control the application flow

Only one package import is used:

```python
import lms
```

Functions are accessed through the package:

```python
lms.add_book()
lms.borrow_book()
lms.return_book()
```

### `lms/books.py`

Contains the main book management functions:

```text
load_books()
save_books()
add_book()
borrow_book()
return_book()
search_book()
view_available_books()
view_all_books()
get_book_by_id()
```

### `lms/borrow_history.py`

Manages borrowing and returning history.

Functions:

```text
load_history()
save_history()
add_history()
display_history()
```

History is automatically saved whenever a book is successfully borrowed or returned.

### `lms/validation.py`

Handles input validation:

```text
validate_book_id()
validate_title()
validate_author()
validate_borrower()
```

### `lms/exceptions.py`

Contains custom exceptions:

```text
LibraryManagementError
```

Exception hierarchy:

```text
LibraryError
│
├── LibraryManagementError
```

### `lms/logger.py`

Provides logging functionality:

```text
setup_logger()
log_message()
```

Logs are stored in:

```text
library.log
```

### `lms/__init__.py`

Acts as the public interface for the `lms` package and exposes functions from the individual modules.

This allows `main.py` to use:

```python
import lms
```

instead of importing every module separately.

## Data Storage

The application uses JSON files for persistent storage.

### `books.json`

Stores library books.

Example:

```json
[
  {
    "id": 1,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "available": true,
    "borrower": null
  }
]
```

When a book is borrowed:

```json
[
  {
    "id": 1,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "available": false,
    "borrower": "Vikrant"
  }
]
```

### `borrowing_history.json`

Stores every successful borrow and return event.

Example:

```json
[
  {
    "book_id": 1,
    "title": "Python Crash Course",
    "borrower": "Vikrant",
    "action": "BORROW",
    "date": "2026-08-10 10:30:15"
  },
  {
    "book_id": 1,
    "title": "Python Crash Course",
    "borrower": "Vikrant",
    "action": "RETURN",
    "date": "2026-08-10 11:15:20"
  }
]
```

## Logging

The application records important events in:

```text
library.log
```

Example:

```text
2026-08-10 10:30:15 - INFO - BOOK ADDED | ID: 1
2026-08-10 10:31:10 - INFO - BOOK BORROWED | ID: 1
2026-08-10 11:15:20 - INFO - BOOK RETURNED | ID: 1
2026-08-10 11:20:05 - ERROR - Book with ID 999 was not found.
```

Logging levels supported:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

## Exception Handling

The application handles the following scenarios.

```python
LibraryManagementError
```

## Exception Demonstration

The project intentionally supports invalid scenarios to demonstrate exception handling.

Examples include:

- Invalid book ID such as `ABC`
- Non-existent book ID such as `999`
- Borrowing an already borrowed book
- Empty book title
- Empty author name
- Empty borrower name

## How to Run

### 1. Open the project directory

Open the project in VS Code or another Python IDE.

### 2. Open the terminal

Navigate to the project directory:

```bash
cd library_management_system
```

### 3. Run the application

```bash
python main.py
```

## Application Menu

```text
========================================
LIBRARY MANAGEMENT SYSTEM
========================================

1. Add Book
2. Borrow Book
3. Return Book
4. Search Book
5. View Available Books
6. View All Books
7. View History
8. Exit
```

## Example Usage

### Add Book

```text
Enter choice: 1

Title: Python Crash Course
Author: Eric Matthes

Book added successfully.
Book ID: 1
```

### Borrow Book

```text
Enter choice: 2

Book ID: 1
Borrower: Vikrant

Book 'Python Crash Course' borrowed successfully by Vikrant.
```

The application automatically:

1. Updates `books.json`
2. Adds a record to `borrowing_history.json`
3. Writes a borrow event to `library.log`

### Return Book

```text
Enter choice: 3

Book ID: 1

Book 'Python Crash Course' returned successfully.
```

The application automatically records the return in the borrowing history.

### Search Book

```text
Enter choice: 4

Search: Python
```

The application searches by:

- Book ID
- Book title
- Author

### View Available Books

```text
Enter choice: 5
```

Displays only books that are currently available.

### View History

```text
Enter choice: 7
```

Displays all borrow and return events.

## Design Approach

The project follows a modular structure:

```text
main.py
   │
   └── lms package
          │
          ├── books.py
          │      └── Book operations
          │
          ├── borrow_history.py
          │      └── Borrowing history
          │
          ├── validation.py
          │      └── Input validation
          │
          ├── exceptions.py
          │      └── Custom exceptions
          │
          └── logger.py
                 └── Application logging
```

The project uses **functions instead of classes**, making it suitable for demonstrating Python fundamentals such as:

- Functions
- Packages
- Modules
- File handling
- JSON
- Exception handling
- Logging
- Input validation

## Requirements

- Python 3.x
- No external Python packages are required.

## Learning Objectives

This project demonstrates practical use of:

- Creating a custom Python package
- Importing functions through `__init__.py`
- Writing reusable functions
- Handling built-in and custom exceptions
- Reading and writing JSON files
- Maintaining application state
- Maintaining borrowing history
- Implementing application logging
- Validating user input
- Building a menu-driven console application

## Future Improvements

Possible future enhancements:

- Delete a book
- Update book information
- Register library members
- Limit the number of books a member can borrow
- Due dates and overdue tracking
- Fine calculation
- Member borrowing history
- Admin/user login
- SQLite or PostgreSQL database
- Unit tests
- Search filters and sorting

## Author

**Library Management System**

Built as a Python console application to practice **functions, packages, modules, exception handling, logging, file handling, and JSON persistence**.
