"""CSV file storage functions."""

import csv
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

EMPLOYEE_FILE = log_file_path / "employees.csv"
PAYROLL_FILE = log_file_path / "payroll_records.csv"


def initialize_files():
    """Create CSV files if they do not exist."""

    if not EMPLOYEE_FILE.exists():

        with EMPLOYEE_FILE.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "employee_id",
                "name",
                "department",
                "monthly_salary",
                "bonus_percentage",
            ])

    if not PAYROLL_FILE.exists():

        with PAYROLL_FILE.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "employee_id",
                "employee_name",
                "month",
                "gross_salary",
                "tax",
                "bonus",
                "net_salary",
            ])


def load_employees():
    """Load employees from CSV."""

    initialize_files()

    employees = []

    with EMPLOYEE_FILE.open(
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            employees.append(row)

    return employees


def save_employees(employees):
    """Save employees to CSV."""

    with EMPLOYEE_FILE.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "employee_id",
            "name",
            "department",
            "monthly_salary",
            "bonus_percentage",
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(employees)


def save_payroll_record(record):
    """Append payroll record to CSV."""

    initialize_files()

    with PAYROLL_FILE.open(
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "employee_id",
            "employee_name",
            "month",
            "gross_salary",
            "tax",
            "bonus",
            "net_salary",
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writerow(record)
