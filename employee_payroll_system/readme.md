# Employee Payroll Calculator

A command-line **Employee Payroll Calculator** built with Python.

This project is intentionally implemented using a **function-based programming approach**. It does **not** use classes, objects, constructors, `self`, inheritance, or other Object-Oriented Programming concepts.

The application demonstrates how a Python project can be organized into multiple modules and a custom package while keeping responsibilities separated.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Complete File Explanation](#complete-file-explanation)
5. [Package Design](#package-design)
6. [Application Architecture](#application-architecture)
7. [Application Flow](#application-flow)
8. [Employee Management](#employee-management)
9. [Salary Calculation](#salary-calculation)
10. [Bonus Calculation](#bonus-calculation)
11. [Tax Calculation](#tax-calculation)
12. [Payslip Generation](#payslip-generation)
13. [Input Validation](#input-validation)
14. [Custom Exception Handling](#custom-exception-handling)
15. [CSV Data Storage](#csv-data-storage)
16. [Logging](#logging)
17. [Why Multiple Modules](#why-multiple-modules)
18. [Why a Custom Package](#why-a-custom-package)
19. [No OOP](#no-oop)
20. [How to Run](#how-to-run)
21. [Application Menu](#application-menu)
22. [Example Usage](#example-usage)
23. [Example CSV Data](#example-csv-data)
24. [Example Log Data](#example-log-data)
25. [Exception Handling Examples](#exception-handling-examples)
26. [Python Concepts Demonstrated](#python-concepts-demonstrated)
27. [Testing Checklist](#testing-checklist)
28. [Future Improvements](#future-improvements)
29. [Conclusion](#conclusion)

---

# Project Overview

The Employee Payroll Calculator allows a user to manage employee information and perform payroll operations from the command line.

The application supports:

- Adding employees
- Viewing employees
- Calculating employee salary
- Calculating bonus
- Calculating tax
- Generating payslips
- Saving employee information
- Saving payroll records
- Validating user input
- Handling application errors
- Logging successful payroll operations
- Logging errors

The application uses CSV files for persistence instead of a database.

The project also uses a custom Python package named `payroll`.

---

# Features

- Add Employee
- Calculate Salary
- Calculate Tax
- Calculate Bonus
- Generate Payslip
- View Employees
- Input validation
- Invalid salary handling
- Invalid bonus handling
- Missing employee handling
- Duplicate employee handling
- Custom exception handling
- Employee CSV storage
- Payroll CSV storage
- Payroll operation logging
- Error logging
- Function-based implementation without OOP

---

# Project Structure

```text
employee_payroll_calculator/
│
├── main.py
├── README.md
│
├── employees.csv
├── payroll_records.csv
├── payroll.log
├── error.log
│
└── payroll/
    │
    ├── __init__.py
    ├── calculations.py
    ├── employees.py
    ├── exceptions.py
    ├── logger.py
    ├── storage.py
    └── validators.py
```

---

# Complete File Explanation

This section explains the purpose and responsibility of **every file** in the project.

## 1. `main.py`

`main.py` is the main entry point of the application.

It is responsible for:

- Displaying the main menu
- Accepting the user's choice
- Calling the appropriate function
- Handling custom payroll exceptions
- Handling unexpected exceptions
- Logging errors
- Keeping the application running until Exit is selected

Main functions:

```python
display_menu()
main()
```

The application starts from:

```python
if __name__ == "__main__":
    main()
```

The main flow is:

```text
User
 |
 v
main.py
 |
 +-- Add Employee
 +-- Calculate Salary
 +-- Calculate Tax
 +-- Calculate Bonus
 +-- Generate Payslip
 +-- View Employees
 +-- Exit
```

---

## 2. `README.md`

This file contains complete project documentation.

It explains:

- Project purpose
- Features
- Folder structure
- Every source file
- Package design
- Module responsibilities
- Calculations
- Validation
- Exception handling
- CSV persistence
- Logging
- Application flow
- How to run the project
- Examples
- Testing checklist
- Future improvements

---

## 3. `payroll/`

`payroll` is the custom Python package.

It contains the application's business logic and supporting modules.

```text
payroll/
├── __init__.py
├── calculations.py
├── employees.py
├── exceptions.py
├── logger.py
├── storage.py
└── validators.py
```

Each module has a clearly defined responsibility.

---

## 4. `payroll/__init__.py`

This file initializes the custom `payroll` package.

It can expose commonly used functions from the package, including:

```python
calculate_bonus()
calculate_tax()
calculate_gross_salary()
calculate_net_salary()

add_employee()
find_employee()
generate_payslip()
```

The package groups all payroll-related functionality in one place.

---

## 5. `payroll/employees.py`

This module contains the main employee and payroll business logic.

Responsibilities:

- Add employee
- Find employee
- Calculate employee salary
- Calculate employee tax
- Calculate employee bonus
- Generate payslip
- Display employees
- Handle interactive operations

Important functions:

```python
add_employee()
find_employee()
calculate_employee_salary()
calculate_employee_tax()
calculate_employee_bonus()
generate_payslip()
display_employees()
```

Interactive functions include:

```python
add_employee_interactive()
calculate_salary_interactive()
calculate_tax_interactive()
calculate_bonus_interactive()
generate_payslip_interactive()
```

### `add_employee()`

The function:

1. Validates employee ID.
2. Validates employee name.
3. Validates department.
4. Validates salary.
5. Validates bonus percentage.
6. Loads existing employees.
7. Checks for duplicate employee ID.
8. Creates an employee dictionary.
9. Saves the employee to `employees.csv`.
10. Logs the successful operation.

Flow:

```text
add_employee()
      |
      v
Validate Input
      |
      v
Load Employees
      |
      v
Check Duplicate ID
      |
      v
Create Employee Record
      |
      v
Save employees.csv
      |
      v
Write payroll.log
```

### `find_employee()`

Searches for an employee using the employee ID.

If found, it returns the employee record.

If not found, it raises:

```python
EmployeeNotFoundError
```

### `calculate_employee_salary()`

This function coordinates the complete salary calculation:

1. Finds the employee.
2. Validates salary.
3. Validates bonus percentage.
4. Calculates bonus.
5. Calculates gross salary.
6. Calculates tax.
7. Calculates net salary.
8. Logs the operation.
9. Returns the payroll information.

### `calculate_employee_tax()`

Calculates tax for a specific employee.

### `calculate_employee_bonus()`

Calculates bonus for a specific employee.

### `generate_payslip()`

This function:

1. Validates the payroll month.
2. Finds the employee.
3. Calculates salary.
4. Creates a payroll record.
5. Saves it to `payroll_records.csv`.
6. Logs the operation.
7. Returns the payslip data.

---

## 6. `payroll/calculations.py`

This module contains all mathematical payroll calculations.

Functions:

```python
calculate_bonus()
calculate_gross_salary()
calculate_tax()
calculate_net_salary()
```

Keeping calculations separate makes the code easier to test, reuse, and maintain.

### Bonus

```text
Bonus = Monthly Salary × Bonus Percentage / 100
```

For example:

```text
Monthly Salary = 60,000
Bonus Percentage = 10%

Bonus = 60,000 × 10 / 100
Bonus = 6,000
```

### Gross Salary

```text
Gross Salary = Monthly Salary + Bonus
```

### Net Salary

```text
Net Salary = Monthly Salary + Bonus - Tax
```

### Tax

The project uses a simple progressive tax structure for programming practice:

```text
Up to 25,000          → 0%
25,001 - 50,000       → 5%
50,001 - 100,000      → 10%
Above 100,000         → 15%
```

This is a demonstration tax calculation and is **not an official Indian income-tax calculator**.

---

## 7. `payroll/validators.py`

This module validates user input before it is processed.

Functions:

```python
validate_employee_id()
validate_name()
validate_department()
validate_salary()
validate_bonus_percentage()
validate_month()
```

### Employee ID

Cannot be empty.

### Name

Cannot be empty.

### Department

Cannot be empty.

### Salary

Must be numeric and greater than zero.

Invalid examples:

```text
abc
0
-5000
```

### Bonus

Must be between 0 and 100.

Invalid examples:

```text
-5
101
150
abc
```

### Month

Cannot be empty.

---

## 8. `payroll/exceptions.py`

This module contains custom exception classes.

Exceptions:

```python
PayrollError
InvalidInputError
InvalidSalaryError
InvalidBonusError
EmployeeNotFoundError
DuplicateEmployeeError
```

The hierarchy is:

```text
PayrollError
   |
   +-- InvalidInputError
   +-- InvalidSalaryError
   +-- InvalidBonusError
   +-- EmployeeNotFoundError
   +-- DuplicateEmployeeError
```

### `PayrollError`

Base exception for payroll-related errors.

### `InvalidInputError`

Raised when required input is missing or invalid.

### `InvalidSalaryError`

Raised when salary is invalid.

### `InvalidBonusError`

Raised when bonus percentage is invalid.

### `EmployeeNotFoundError`

Raised when the requested employee does not exist.

### `DuplicateEmployeeError`

Raised when an employee ID already exists.

---

## 9. `payroll/storage.py`

This module handles CSV file operations.

Functions:

```python
initialize_files()
load_employees()
save_employees()
save_payroll_record()
```

### `initialize_files()`

Creates the required CSV files and headers if they do not exist.

### `load_employees()`

Reads employees from:

```text
employees.csv
```

### `save_employees()`

Writes employee data to:

```text
employees.csv
```

### `save_payroll_record()`

Appends payroll data to:

```text
payroll_records.csv
```

Separating storage logic keeps CSV handling out of the business logic.

---

## 10. `payroll/logger.py`

This module handles logging using Python's `logging` module.

Functions:

```python
create_logger()
log_payroll()
log_error()
```

Two log files are used:

```text
payroll.log
error.log
```

### `log_payroll()`

Records successful operations such as:

- Employee added
- Salary calculated
- Tax calculated
- Bonus calculated
- Payslip generated

### `log_error()`

Records errors such as:

- Invalid salary
- Employee not found
- Duplicate employee
- Invalid bonus
- Invalid menu choice

---

## 11. `employees.csv`

This is the employee data file.

Header:

```csv
employee_id,name,department,monthly_salary,bonus_percentage
```

Example:

```csv
employee_id,name,department,monthly_salary,bonus_percentage
E001,Rahul,IT,60000.00,10.00
E002,Amit,HR,45000.00,8.00
```

The file provides persistent employee storage.

---

## 12. `payroll_records.csv`

This file stores generated payroll records.

Header:

```csv
employee_id,employee_name,month,gross_salary,tax,bonus,net_salary
```

Example:

```csv
employee_id,employee_name,month,gross_salary,tax,bonus,net_salary
E001,Rahul,August 2026,66000.00,5350.00,6000.00,60650.00
```

Each generated payslip creates a new payroll record.

---

## 13. `payroll.log`

This file stores successful payroll operations.

Example:

```text
2026-08-10 20:30:10 - INFO - Employee added: E001 - Rahul
2026-08-10 20:31:15 - INFO - Salary calculated: E001, net salary=60650.00
2026-08-10 20:32:20 - INFO - Bonus calculated: E001, bonus=6000.00
2026-08-10 20:33:10 - INFO - Payslip generated: E001, month=August 2026
```

It provides an audit trail of important operations.

---

## 14. `error.log`

This file stores application errors.

Example:

```text
2026-08-10 20:35:10 - ERROR - Salary must be greater than zero.
2026-08-10 20:36:15 - ERROR - Employee 'E999' was not found.
```

This helps with debugging and tracking failed operations.

---

# Package Design

The custom package is:

```text
payroll
```

It contains:

```text
payroll/
│
├── __init__.py
│
├── employees.py
│       Employee and payroll business logic
│
├── calculations.py
│       Salary, tax and bonus calculations
│
├── validators.py
│       Input validation
│
├── exceptions.py
│       Custom exceptions
│
├── storage.py
│       CSV persistence
│
└── logger.py
        Logging
```

The package design separates functionality according to responsibility.

---

# Application Architecture

```text
                    USER
                      |
                      v
                  main.py
                      |
                      v
                employees.py
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
 calculations.py  validators.py  exceptions.py
       |
       +--------------------+
       |                    |
       v                    v
  storage.py            logger.py
       |                    |
       v                    v
  CSV Files             Log Files
```

---

# Application Flow

## Add Employee

```text
User
 |
 v
main.py
 |
 v
add_employee_interactive()
 |
 v
add_employee()
 |
 v
Validate Input
 |
 v
Check Duplicate
 |
 v
Save employees.csv
 |
 v
Write payroll.log
 |
 v
Display Success
```

## Calculate Salary

```text
User
 |
 v
main.py
 |
 v
calculate_salary_interactive()
 |
 v
calculate_employee_salary()
 |
 +-- find_employee()
 |
 +-- validate_salary()
 |
 +-- calculate_bonus()
 |
 +-- calculate_gross_salary()
 |
 +-- calculate_tax()
 |
 +-- calculate_net_salary()
 |
 v
Write payroll.log
 |
 v
Display Result
```

## Generate Payslip

```text
User
 |
 v
main.py
 |
 v
generate_payslip_interactive()
 |
 v
generate_payslip()
 |
 +-- Validate Month
 |
 +-- Find Employee
 |
 +-- Calculate Salary
 |
 +-- Create Payroll Record
 |
 v
Save payroll_records.csv
 |
 v
Write payroll.log
 |
 v
Display Payslip
```

---

# Why Multiple Modules?

The application could be implemented in one large file, but separating the code has several advantages.

## Separation of Responsibilities

Each module has a clear job:

```text
main.py           → Application flow
employees.py      → Business logic
calculations.py   → Calculations
validators.py     → Validation
exceptions.py     → Errors
storage.py        → CSV persistence
logger.py         → Logging
```

## Maintainability

If CSV storage changes, only `storage.py` needs to be modified.

If salary formulas change, `calculations.py` can be modified.

If validation rules change, `validators.py` can be modified.

## Reusability

Functions can be imported and reused by other modules.

## Testing

Individual functions can be tested independently.

## Readability

A reviewer can quickly identify where each feature is implemented.

---

# Why Use a Custom Package?

The `payroll` package groups all payroll-related modules together.

Without a package, the root directory would contain many unrelated Python files.

With a package:

```text
employee_payroll_calculator/
│
├── main.py
│
└── payroll/
    ├── calculations.py
    ├── employees.py
    ├── exceptions.py
    ├── logger.py
    ├── storage.py
    └── validators.py
```

This makes the project structure cleaner and demonstrates Python package organization.

---

# No OOP

This project intentionally does not use Object-Oriented Programming.

There are:

- No classes
- No objects
- No `self`
- No constructors
- No inheritance
- No class methods

Instead, the project uses:

- Functions
- Lists
- Dictionaries
- Modules
- Packages
- CSV files
- Exception handling
- Logging

Employee data is represented using dictionaries.

Example:

```python
employee = {
    "employee_id": "E001",
    "name": "Rahul",
    "department": "IT",
    "monthly_salary": "60000.00",
    "bonus_percentage": "10.00"
}
```

Operations are performed through functions.

---

# How to Run

## 1. Open the Project

Open the `employee_payroll_calculator` folder in VS Code.

## 2. Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

## 3. Run

```bash
python main.py
```

If your environment uses `python3`:

```bash
python3 main.py
```

No third-party packages are required.

The project uses Python standard-library modules such as:

```text
csv
logging
pathlib
```

---

# Application Menu

```text
========================================
       EMPLOYEE PAYROLL CALCULATOR
========================================
1. Add Employee
2. Calculate Salary
3. Calculate Tax
4. Calculate Bonus
5. Generate Payslip
6. View Employees
7. Exit
========================================
```

---

# Example Usage

## Add Employee

Select:

```text
1
```

Enter:

```text
Employee ID: E001
Employee Name: Rahul
Department: IT
Monthly Salary: 60000
Bonus Percentage: 10
```

Output:

```text
Employee 'Rahul' added successfully.
```

The employee is saved to:

```text
employees.csv
```

The successful operation is written to:

```text
payroll.log
```

---

## View Employees

Select:

```text
6
```

Example:

```text
Employee List
--------------------------------------------------------------------------------
ID          Name                Department                  Salary
--------------------------------------------------------------------------------
E001        Rahul               IT                       60000.00
E002        Amit                HR                       45000.00
--------------------------------------------------------------------------------
```

---

## Calculate Salary

Select:

```text
2
```

Enter:

```text
Employee ID: E001
```

Example:

```text
Salary Details
-----------------------------------
Employee     : Rahul
Basic Salary : 60000.00
Bonus        : 6000.00
Gross Salary : 66000.00
Tax          : 5350.00
Net Salary   : 60650.00
```

---

## Calculate Tax

Select:

```text
3
```

Enter:

```text
Employee ID: E001
```

Example:

```text
Tax: 5350.00
```

---

## Calculate Bonus

Select:

```text
4
```

Enter:

```text
Employee ID: E001
```

Example:

```text
Bonus: 6000.00
```

---

## Generate Payslip

Select:

```text
5
```

Enter:

```text
Employee ID: E001
Payroll Month: August 2026
```

Example:

```text
=============================================
              PAYSLIP
=============================================
Employee ID : E001
Employee    : Rahul
Month       : August 2026
---------------------------------------------
Gross Salary: 66000.00
Bonus       : 6000.00
Tax         : 5350.00
Net Salary  : 60650.00
=============================================
```

The record is saved to:

```text
payroll_records.csv
```

The operation is logged in:

```text
payroll.log
```

---

# Exception Handling Examples

## Invalid Salary

Input:

```text
Monthly Salary: -5000
```

Output:

```text
Error: Salary must be greater than zero.
```

The error is also recorded in `error.log`.

---

## Non-Numeric Salary

Input:

```text
Monthly Salary: abc
```

Output:

```text
Error: Salary must be a valid number.
```

---

## Missing Employee

Input:

```text
Employee ID: E999
```

Output:

```text
Error: Employee 'E999' was not found.
```

---

## Duplicate Employee

If `E001` already exists:

```text
Employee ID: E001
```

Output:

```text
Error: Employee 'E001' already exists.
```

---

## Invalid Bonus

Input:

```text
Bonus Percentage: 150
```

Output:

```text
Error: Bonus percentage must be between 0 and 100.
```

---

## Empty Name

Input:

```text
Employee Name:
```

Output:

```text
Error: Employee name cannot be empty.
```

---

## Invalid Menu Choice

Input:

```text
Enter your choice: 10
```

Output:

```text
Error: Invalid choice. Please enter a number from 1 to 7.
```

---

# CSV Data Flow

## Employee Data

```text
Add Employee
     |
     v
employees.py
     |
     v
storage.py
     |
     v
employees.csv
```

## Payroll Data

```text
Generate Payslip
     |
     v
employees.py
     |
     v
storage.py
     |
     v
payroll_records.csv
```

---

# Logging Data Flow

## Successful Operation

```text
Payroll Operation
       |
       v
logger.py
       |
       v
payroll.log
```

## Error

```text
Exception
    |
    v
main.py
    |
    v
logger.py
    |
    v
error.log
```

---

# Example CSV Data

## `employees.csv`

```csv
employee_id,name,department,monthly_salary,bonus_percentage
E001,Rahul,IT,60000.00,10.00
E002,Amit,HR,45000.00,8.00
E003,Priya,Finance,75000.00,12.00
```

## `payroll_records.csv`

```csv
employee_id,employee_name,month,gross_salary,tax,bonus,net_salary
E001,Rahul,August 2026,66000.00,5350.00,6000.00,60650.00
E002,Amit,August 2026,48600.00,1180.00,3600.00,47420.00
```

---

# Example Log Data

## `payroll.log`

```text
2026-08-10 20:30:10 - INFO - Employee added: E001 - Rahul
2026-08-10 20:31:15 - INFO - Salary calculated: E001, net salary=60650.00
2026-08-10 20:32:20 - INFO - Bonus calculated: E001, bonus=6000.00
2026-08-10 20:33:10 - INFO - Tax calculated: E001, tax=5350.00
2026-08-10 20:34:05 - INFO - Payslip generated: E001, month=August 2026
```

## `error.log`

```text
2026-08-10 20:35:10 - ERROR - Salary must be greater than zero.
2026-08-10 20:36:15 - ERROR - Employee 'E999' was not found.
2026-08-10 20:37:20 - ERROR - Employee 'E001' already exists.
```

---

# Complete Responsibility Table

| File                      | Type          | Responsibility                                                  |
| ------------------------- | ------------- | --------------------------------------------------------------- |
| `main.py`                 | Python module | Application entry point, menu and high-level exception handling |
| `README.md`               | Documentation | Complete project documentation                                  |
| `payroll/__init__.py`     | Package file  | Initializes and exposes the custom package                      |
| `payroll/employees.py`    | Python module | Employee and payroll business logic                             |
| `payroll/calculations.py` | Python module | Salary, bonus, tax and net salary calculations                  |
| `payroll/validators.py`   | Python module | Input validation                                                |
| `payroll/exceptions.py`   | Python module | Custom exception definitions                                    |
| `payroll/storage.py`      | Python module | CSV file creation, reading and writing                          |
| `payroll/logger.py`       | Python module | Payroll and error logging                                       |
| `employees.csv`           | Data file     | Persistent employee records                                     |
| `payroll_records.csv`     | Data file     | Persistent payroll records                                      |
| `payroll.log`             | Log file      | Successful payroll operations                                   |
| `error.log`               | Log file      | Application errors                                              |

---

# Testing Checklist

Before submission, test the following.

## Employee

- [ ] Add valid employee
- [ ] Add duplicate employee
- [ ] Empty employee ID
- [ ] Empty employee name
- [ ] Empty department

## Salary

- [ ] Valid salary
- [ ] Zero salary
- [ ] Negative salary
- [ ] Text as salary

## Bonus

- [ ] Valid bonus
- [ ] Zero bonus
- [ ] Negative bonus
- [ ] Bonus greater than 100
- [ ] Text as bonus

## Employee Lookup

- [ ] Existing employee
- [ ] Missing employee

## Payroll

- [ ] Calculate salary
- [ ] Calculate tax
- [ ] Calculate bonus
- [ ] Generate payslip
- [ ] Verify `payroll_records.csv`

## Logging

- [ ] Verify successful operations in `payroll.log`
- [ ] Verify errors in `error.log`

## Persistence

- [ ] Add employee
- [ ] Exit application
- [ ] Start application again
- [ ] Verify employee still exists
- [ ] Generate payslip
- [ ] Verify payroll record exists

---

# Design Principles

The project follows these principles:

## Separation of Responsibilities

Every module has a clear responsibility.

## Reusability

Functions are designed to be reused by other modules.

## Centralized Validation

Validation is handled by `validators.py`.

## Centralized Exceptions

Custom exceptions are defined in `exceptions.py`.

## Centralized Storage

CSV operations are handled by `storage.py`.

## Centralized Logging

Logging is handled by `logger.py`.

## Function-Based Programming

All application operations are implemented using functions rather than classes.

---

# Python Concepts Demonstrated

The project demonstrates:

## Basic Python

- Variables
- Strings
- Numbers
- Lists
- Dictionaries
- Conditions
- Loops

## Functions

- Function definitions
- Parameters
- Return values
- Function calls
- Reusable functions
- Interactive functions

## Modules

Code is divided into multiple Python modules.

## Packages

A custom `payroll` package is created.

## File Handling

The project reads and writes persistent files.

## CSV

Python's `csv` module is used for employee and payroll storage.

## Exception Handling

The project uses:

```python
try
except
```

and custom exception classes.

## Logging

Python's standard `logging` module is used.

## Input Validation

User input is validated before processing.

---

# Future Improvements

The current architecture can be extended with:

1. Update employee
2. Delete employee
3. Search employee
4. Employee attendance
5. Monthly payroll reports
6. Annual payroll reports
7. Department-wise reports
8. JSON export
9. Database storage
10. Unit tests
11. Automated report generation
12. Configurable tax slabs
13. Payroll history search
14. Graphical user interface

The modular design makes these additions easier because new functionality can be added without putting all code into one file.

---

# Final Summary

The Employee Payroll Calculator is a complete **function-based Python project**.

It uses:

```text
Python
  |
  +-- Functions
  +-- Multiple Modules
  +-- Custom Package
  +-- Custom Exceptions
  +-- Input Validation
  +-- CSV Persistence
  +-- Logging
  +-- File Handling
```

The main responsibilities are separated as follows:

```text
main.py
    ↓
Application flow

employees.py
    ↓
Employee and payroll operations

calculations.py
    ↓
Salary, bonus and tax calculations

validators.py
    ↓
Input validation

exceptions.py
    ↓
Custom errors

storage.py
    ↓
CSV persistence

logger.py
    ↓
Payroll and error logging
```

This modular structure makes the application easier to understand, maintain, test, debug, reuse, and extend.

The project intentionally avoids OOP and implements the required payroll functionality using functions, modules, a custom package, exception handling, CSV storage, and logging.
