# Student Management System

A simple Python CLI application for managing student records.

## Project Structure

- `main.py` - Entry point for the CLI.
- `students/` - Package containing student management logic.
  - `manager.py` - CRUD operations for student records.
  - `storage.py` - Persistence layer for `students.json`.
  - `exceptions.py` - Custom exception class.
  - `logger.py` - Simple logging to `student.log`.
  - `__init__.py` - Package exports for `import students`.
- `students.json` - Data file for storing student records.
- `student.log` - Log file for application events.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies if needed (currently no external packages required).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Usage

Run the CLI from the `student_management_system` folder:

```powershell
cd july30python\week-3\student_management_system
.\.venv\Scripts\python.exe .\main.py
```

Follow the menu prompts to add, remove, update, search, and display students.

## Notes

- `students.json` is used as the main data store.
- `students/__init__.py` exports the package API so the app can use `import students`.
- Empty `students.json` files are treated as an empty student store.
