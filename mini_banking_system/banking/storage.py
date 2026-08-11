"""CSV file initialization, reading, and writing functions."""

import csv
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
CUSTOMERS_FILE = PROJECT_FOLDER / "customers.csv"
TRANSACTIONS_FILE = PROJECT_FOLDER / "transactions.csv"

CUSTOMER_HEADERS = ["account_number", "name", "balance"]
TRANSACTION_HEADERS = [
    "transaction_id", "date_time", "account_number", "transaction_type",
    "amount", "balance", "details", "status"
]


def _create_csv_if_missing(file_path, headers):
    """Create one CSV file and its header when necessary."""
    if not file_path.exists() or file_path.stat().st_size == 0:
        with file_path.open("w", newline="", encoding="utf-8") as csv_file:
            csv.DictWriter(csv_file, fieldnames=headers).writeheader()


def initialize_files():
    """Create both CSV files with the required headers if missing."""
    _create_csv_if_missing(CUSTOMERS_FILE, CUSTOMER_HEADERS)
    _create_csv_if_missing(TRANSACTIONS_FILE, TRANSACTION_HEADERS)


def load_customers():
    """Load all customers as a list of dictionaries."""
    initialize_files()
    with CUSTOMERS_FILE.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def save_customers(customers):
    """Replace customers.csv with the supplied customer dictionaries."""
    with CUSTOMERS_FILE.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CUSTOMER_HEADERS)
        writer.writeheader()
        writer.writerows(customers)


def save_transaction(transaction):
    """Append one transaction dictionary to transactions.csv."""
    initialize_files()
    with TRANSACTIONS_FILE.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=TRANSACTION_HEADERS)
        writer.writerow(transaction)


def load_transactions():
    """Load all transactions as a list of dictionaries."""
    initialize_files()
    with TRANSACTIONS_FILE.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))
