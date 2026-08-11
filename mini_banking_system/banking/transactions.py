"""Functions for deposits, withdrawals, transfers, history, and reports."""

from decimal import Decimal

from .customers import find_customer
from .exceptions import InsufficientBalanceError, SameAccountTransferError
from .logger import log_error, log_transaction
from .storage import load_customers, load_transactions, save_customers, save_transaction
from .utilities import current_datetime, format_money, generate_transaction_id
from .validation import validate_account_number, validate_amount


def _update_customer_balance(account_number, new_balance):
    """Update one balance and persist the complete customer list."""
    customers = load_customers()
    for customer in customers:
        if customer["account_number"] == account_number:
            customer["balance"] = f"{new_balance:.2f}"
            break
    save_customers(customers)


def _transaction(account_number, transaction_type, amount, balance, details, status):
    """Build and save one transaction dictionary."""
    transaction = {
        "transaction_id": generate_transaction_id(),
        "date_time": current_datetime(),
        "account_number": account_number,
        "transaction_type": transaction_type,
        "amount": f"{Decimal(str(amount)):.2f}",
        "balance": f"{Decimal(str(balance)):.2f}",
        "details": details,
        "status": status,
    }
    save_transaction(transaction)
    return transaction


def deposit(account_number, amount):
    """Add a positive amount to an existing account."""
    customer = find_customer(account_number)
    amount = validate_amount(amount)
    new_balance = Decimal(customer["balance"]) + amount
    _update_customer_balance(customer["account_number"], new_balance)
    transaction = _transaction(
        customer["account_number"], "DEPOSIT", amount, new_balance, "Cash deposit", "SUCCESS"
    )
    log_transaction(
        f"Deposit successful | id={transaction['transaction_id']} | "
        f"account={customer['account_number']} | amount={amount:.2f}"
    )
    return float(new_balance)


def withdraw(account_number, amount):
    """Remove money or save a FAILED transaction if funds are insufficient."""
    customer = find_customer(account_number)
    amount = validate_amount(amount)
    current_balance = Decimal(customer["balance"])
    if amount > current_balance:
        details = "Insufficient balance for withdrawal"
        transaction = _transaction(
            customer["account_number"], "WITHDRAW", amount, current_balance, details, "FAILED"
        )
        message = (
            f"Insufficient balance | id={transaction['transaction_id']} | "
            f"account={customer['account_number']} | amount={amount:.2f} | balance={current_balance:.2f}"
        )
        log_error(message)
        raise InsufficientBalanceError(details)

    new_balance = current_balance - amount
    _update_customer_balance(customer["account_number"], new_balance)
    transaction = _transaction(
        customer["account_number"], "WITHDRAW", amount, new_balance, "Cash withdrawal", "SUCCESS"
    )
    log_transaction(
        f"Withdrawal successful | id={transaction['transaction_id']} | "
        f"account={customer['account_number']} | amount={amount:.2f}"
    )
    return float(new_balance)


def transfer_money(sender_account, receiver_account, amount):
    """Transfer money and save matching TRANSFER OUT and TRANSFER IN records."""
    sender_number = validate_account_number(sender_account)
    receiver_number = validate_account_number(receiver_account)
    if sender_number == receiver_number:
        message = f"Sender and receiver cannot be the same account: {sender_number}"
        log_error(message)
        raise SameAccountTransferError(message)

    sender = find_customer(sender_number)
    receiver = find_customer(receiver_number)
    amount = validate_amount(amount)
    sender_balance = Decimal(sender["balance"])
    receiver_balance = Decimal(receiver["balance"])

    if amount > sender_balance:
        details = f"Transfer to {receiver_number} failed: insufficient balance"
        transaction = _transaction(
            sender_number, "TRANSFER OUT", amount, sender_balance, details, "FAILED"
        )
        message = (
            f"Insufficient balance for transfer | id={transaction['transaction_id']} | "
            f"sender={sender_number} | receiver={receiver_number} | amount={amount:.2f}"
        )
        log_error(message)
        raise InsufficientBalanceError(details)

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount
    customers = load_customers()
    for customer in customers:
        if customer["account_number"] == sender_number:
            customer["balance"] = f"{new_sender_balance:.2f}"
        elif customer["account_number"] == receiver_number:
            customer["balance"] = f"{new_receiver_balance:.2f}"
    save_customers(customers)

    outgoing = _transaction(
        sender_number, "TRANSFER OUT", amount, new_sender_balance,
        f"Transferred to {receiver_number}", "SUCCESS"
    )
    _transaction(
        receiver_number, "TRANSFER IN", amount, new_receiver_balance,
        f"Received from {sender_number}", "SUCCESS"
    )
    log_transaction(
        f"Transfer successful | id={outgoing['transaction_id']} | sender={sender_number} | "
        f"receiver={receiver_number} | amount={amount:.2f}"
    )
    return float(new_sender_balance), float(new_receiver_balance)


def get_transaction_history(account_number):
    """Return all transactions for one existing account."""
    customer = find_customer(account_number)
    return [
        transaction for transaction in load_transactions()
        if transaction["account_number"] == customer["account_number"]
    ]


def generate_transaction_report():
    """Calculate and return transaction totals in a dictionary."""
    transactions = load_transactions()
    successful = [item for item in transactions if item["status"] == "SUCCESS"]
    failed = [item for item in transactions if item["status"] == "FAILED"]
    return {
        "total_transactions": len(transactions),
        "successful_transactions": len(successful),
        "failed_transactions": len(failed),
        "total_deposits": sum(
            Decimal(item["amount"]) for item in successful if item["transaction_type"] == "DEPOSIT"
        ),
        "total_withdrawals": sum(
            Decimal(item["amount"]) for item in successful if item["transaction_type"] == "WITHDRAW"
        ),
        "total_transfers": sum(
            Decimal(item["amount"]) for item in successful if item["transaction_type"] == "TRANSFER OUT"
        ),
    }


def deposit_interactive():
    """Collect and process a deposit."""
    account_number = input("Enter account number: ")
    amount = input("Enter deposit amount: ")
    print(f"Deposit successful. New balance: {format_money(deposit(account_number, amount))}")


def withdraw_interactive():
    """Collect and process a withdrawal."""
    account_number = input("Enter account number: ")
    amount = input("Enter withdrawal amount: ")
    print(f"Withdrawal successful. New balance: {format_money(withdraw(account_number, amount))}")


def transfer_interactive():
    """Collect and process a transfer."""
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")
    amount = input("Enter transfer amount: ")
    sender_balance, receiver_balance = transfer_money(sender, receiver, amount)
    print(f"Transfer successful. Sender balance: {format_money(sender_balance)}")
    print(f"Receiver balance: {format_money(receiver_balance)}")


def transaction_history_interactive():
    """Display the complete transaction history for one account."""
    account_number = input("Enter account number: ")
    transactions = get_transaction_history(account_number)
    if not transactions:
        print("No transactions found for this account.")
        return
    for item in transactions:
        print("\nTransaction ID:", item["transaction_id"])
        print("Date/time:", item["date_time"])
        print("Type:", item["transaction_type"])
        print("Amount:", format_money(item["amount"]))
        print("Balance:", format_money(item["balance"]))
        print("Status:", item["status"])
        print("Details:", item["details"])


def generate_report_interactive():
    """Generate and display the transaction report."""
    report = generate_transaction_report()
    print("\nTRANSACTION REPORT")
    print("-" * 35)
    print("Total transactions:", report["total_transactions"])
    print("Successful transactions:", report["successful_transactions"])
    print("Failed transactions:", report["failed_transactions"])
    print("Total deposits:", format_money(report["total_deposits"]))
    print("Total successful withdrawals:", format_money(report["total_withdrawals"]))
    print("Total transfers:", format_money(report["total_transfers"]))
