"""Functions for creating, finding, and displaying customers."""

from .exceptions import AccountNotFoundError, DuplicateAccountError
from .logger import log_error, log_transaction
from .storage import load_customers, save_customers
from .utilities import format_money
from .validation import validate_account_number, validate_initial_balance, validate_name


def find_customer(account_number):
    """Find and return a customer dictionary by account number."""
    account_number = validate_account_number(account_number)
    for customer in load_customers():
        if customer["account_number"] == account_number:
            return customer
    message = f"Account not found: {account_number}"
    log_error(message)
    raise AccountNotFoundError(message)


def create_account(account_number, name, initial_balance):
    """Validate and save a new customer account."""
    account_number = validate_account_number(account_number)
    name = validate_name(name)
    initial_balance = validate_initial_balance(initial_balance)
    customers = load_customers()

    for customer in customers:
        if customer["account_number"] == account_number:
            message = f"Duplicate account: {account_number}"
            log_error(message)
            raise DuplicateAccountError(message)

    new_customer = {
        "account_number": account_number,
        "name": name,
        "balance": f"{initial_balance:.2f}",
    }
    customers.append(new_customer)
    save_customers(customers)
    log_transaction(
        f"Account created | account={account_number} | name={name} | balance={initial_balance:.2f}"
    )
    return new_customer


def check_balance(account_number):
    """Return the current balance for an existing account."""
    customer = find_customer(account_number)
    return float(customer["balance"])


def display_customers():
    """Print all saved customers in a readable table."""
    customers = load_customers()
    if not customers:
        print("No customers found.")
        return customers
    print("\nACCOUNT NUMBER       CUSTOMER NAME                 BALANCE")
    print("-" * 62)
    for customer in customers:
        print(f"{customer['account_number']:<20} {customer['name']:<29} {format_money(customer['balance'])}")
    return customers


def create_account_interactive():
    """Collect account information and create an account."""
    account_number = input("Enter account number: ")
    name = input("Enter customer name: ")
    initial_balance = input("Enter initial balance: ")
    customer = create_account(account_number, name, initial_balance)
    print(f"Account {customer['account_number']} created successfully.")


def check_balance_interactive():
    """Ask for an account number and display its balance."""
    account_number = input("Enter account number: ")
    balance = check_balance(account_number)
    print(f"Current balance: {format_money(balance)}")
