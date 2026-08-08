# Personal Expense Tracker

A beginner-friendly command-line **Personal Expense Tracker** built with Python. The project demonstrates Python functions, modules, custom packages, exception handling, logging, CSV file operations, and report generation.

## Features

- Add Expense
- Delete Expense
- Update Expense
- View All Expenses
- Monthly Expense Summary
- Category-wise Expense Summary
- Find Highest Expense
- Export Monthly Expense Report
- Automatically store expenses in CSV
- Log application operations and errors
- Input validation with exceptions
- Generate monthly reports as text files

## Project Structure

```text
expense_tracker/
│
├── main.py
├── expenses.csv
├── expense.log
│
├── reports/
│   └── monthly_report_YYYY-MM.txt
│
└── expense_manager/
    ├── __init__.py
    ├── expenses.py
    ├── reports.py
    ├── validation.py
    └── logger.py
```

## Module Organization

### `main.py`

The main entry point of the application.

Responsibilities:

- Display the menu
- Accept user input
- Call functions from other modules
- Handle user-facing exceptions
- Display results
- Log application operations

### `expense_manager/expenses.py`

Handles expense data and CSV file operations.

Main responsibilities:

- Initialize the CSV file
- Load expenses
- Save expenses
- Generate unique expense IDs
- Add expenses
- Delete expenses
- Update expenses
- Find an expense by ID

### `expense_manager/reports.py`

Handles calculations and report generation.

Main responsibilities:

- Monthly summary
- Category-wise summary
- Highest expense
- Monthly report export

### `expense_manager/validation.py`

Contains reusable validation functions.

Validates:

- Date
- Amount
- Category
- Description
- Expense ID
- Month

### `expense_manager/logger.py`

Centralizes application logging.

Logs:

- Successful operations
- Validation errors
- File errors
- Warnings
- Application start and exit

### `expense_manager/__init__.py`

Makes `expense_manager` a custom Python package and exposes commonly used functions.

## Requirements

- Python 3.8 or higher
- No external Python packages are required

The project uses Python standard-library modules such as:

- `csv`
- `os`
- `datetime`
- `logging`

## How to Run

Clone or download the project and open a terminal in the project directory.

Run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Application Menu

```text
==================================================
       PERSONAL EXPENSE TRACKER
==================================================
1. Add Expense
2. Delete Expense
3. Update Expense
4. View All Expenses
5. Monthly Summary
6. Category-wise Summary
7. Highest Expense
8. Export Monthly Report
9. Exit
==================================================
Enter your choice:
```

## Expense Data

Expenses are stored in `expenses.csv`.

Example:

```csv
id,date,category,description,amount
1,2026-08-01,Food,Lunch,250.0
2,2026-08-02,Transport,Auto fare,150.0
3,2026-08-03,Shopping,T-shirt,799.0
4,2026-08-05,Food,Dinner,450.0
```

The application creates the CSV file automatically if it does not exist.

## Date Format

Use:

```text
YYYY-MM-DD
```

Example:

```text
2026-08-08
```

For monthly reports, use:

```text
YYYY-MM
```

Example:

```text
2026-08
```

## Exception Handling

The application validates user input and handles expected errors without crashing.

Examples:

- Invalid date → `ValueError`
- Invalid amount → `ValueError`
- Invalid expense ID → `ValueError`
- Invalid month → `ValueError`
- CSV/file operation failure → `OSError`

The project also uses exception chaining where appropriate:

```python
except OSError as e:
    raise OSError(
        f"Error reading expense file: {e}"
    ) from e
```

This preserves the original exception as the cause of the new exception.

## Logging

All important operations are logged to:

```text
expense.log
```

Example:

```text
2026-08-08 20:00:00 - INFO - Expense Tracker application started.
2026-08-08 20:01:10 - INFO - Expense added successfully. ID=1
2026-08-08 20:02:20 - INFO - Monthly summary generated for 2026-08
2026-08-08 20:03:00 - WARNING - Expense not found. ID=99
```

## Monthly Report

Selecting **Export Monthly Report** generates a report automatically.

Example:

```text
reports/monthly_report_2026-08.txt
```

The report contains:

- Expense details
- Total monthly expense
- Category-wise totals
- Highest expense

Example:

```text
==================================================
MONTHLY EXPENSE REPORT - 2026-08
==================================================

EXPENSE DETAILS
--------------------------------------------------
ID: 1 | Date: 2026-08-01 | Category: Food | Description: Lunch | Amount: ₹250.00
ID: 2 | Date: 2026-08-02 | Category: Transport | Description: Auto fare | Amount: ₹150.00

TOTAL EXPENSE: ₹400.00

CATEGORY-WISE SUMMARY
--------------------------------------------------
Food: ₹250.00
Transport: ₹150.00

HIGHEST EXPENSE
--------------------------------------------------
Description: Lunch
Category: Food
Amount: ₹250.00
```

## Function Reuse

The project separates reusable functionality into functions instead of putting all logic inside `main.py`.

For example:

```python
validate_date()
validate_amount()
validate_category()
validate_month()
```

Reporting functions are also reused:

```python
monthly_summary()
category_summary()
highest_expense()
```

The report generator combines these existing functions instead of duplicating their logic:

```python
expenses, total = monthly_summary(month)
category_data = category_summary(month)
highest = highest_expense(month)
```

## File Operations

The project uses CSV files for persistent expense storage.

### Reading CSV

```python
with open(
    FILE_NAME,
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.DictReader(file)
```

### Writing CSV

```python
with open(
    FILE_NAME,
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )
```

UTF-8 encoding is explicitly specified so the application can safely handle characters such as the Indian Rupee symbol (`₹`) in reports.

## Program Flow

```text
User
  │
  ▼
main.py
  │
  ├── validation.py
  │      └── Validate user input
  │
  ├── expenses.py
  │      └── Read/Write expenses.csv
  │
  ├── reports.py
  │      └── Generate summaries/reports
  │
  └── logger.py
         └── Write operations to expense.log
```

## Learning Objectives

This project demonstrates:

- Python functions
- Function reuse
- Modules
- Custom packages
- Imports
- Lists and dictionaries
- List comprehensions
- Lambda functions
- CSV file handling
- Text file handling
- Exception handling
- Exception chaining
- Logging
- Input validation
- File and directory operations
- Basic report generation

## Future Improvements

Possible enhancements for future versions:

- Add expense search
- Add income tracking
- Add budget management
- Add budget alerts
- Add yearly reports
- Export reports to CSV/PDF
- Add charts and visualizations
- Add SQLite database support
- Add a graphical user interface
- Add unit tests
- Add configuration management

## Author

**Personal Expense Tracker**

Built as a Python learning project to practice modular programming, file handling, validation, exception handling, and logging.
