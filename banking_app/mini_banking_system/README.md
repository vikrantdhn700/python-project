# Mini Banking System

## Project overview

Mini Banking System is a beginner-friendly, command-line Python project. It uses
functions, modules, dictionaries, lists, CSV files, custom exceptions, and logging.
The application has no banking classes and does not use `self` or object-oriented
design. The only class declarations are the custom exception types, because Python
requires an exception to inherit from `Exception` before it can be raised and caught.

## Features

1. Create Account
2. Deposit
3. Withdraw
4. Transfer Money
5. Check Balance
6. Transaction History
7. Generate Transaction Report
8. View Customers
9. Exit

## Folder structure

```text
mini_banking_system/
|-- main.py
|-- README.md
|-- customers.csv
|-- transactions.csv
|-- banking.log
|-- error.log
`-- banking/
    |-- __init__.py
    |-- customers.py
    |-- transactions.py
    |-- utilities.py
    |-- validation.py
    |-- exceptions.py
    |-- storage.py
    `-- logger.py
```

## File responsibilities

- `main.py`: displays the menu, receives choices, calls package functions, catches
  expected `BankingError` exceptions and unexpected errors, and logs problems.
- `customers.csv`: persists account numbers, names, and balances.
- `transactions.csv`: keeps the complete successful and failed transaction audit trail.
- `banking.log`: records successful account and money operations.
- `error.log`: records failed operations, invalid choices, and application errors.
- `banking/__init__.py`: marks `banking` as a custom Python package and exports its
  most useful functions.
- `banking/customers.py`: creates and finds accounts, checks balances, lists customers,
  and provides customer-related interactive functions.
- `banking/transactions.py`: handles deposits, withdrawals, transfers, history,
  reports, and their interactive functions.
- `banking/utilities.py`: generates transaction IDs and timestamps and formats money.
- `banking/validation.py`: validates account numbers, names, transaction amounts, and
  initial balances.
- `banking/exceptions.py`: defines all expected banking exception types.
- `banking/storage.py`: initializes, reads, and writes the CSV files with Python's
  standard `csv` module.
- `banking/logger.py`: creates the success and error loggers and exposes simple
  logging functions.

## Why separate modules?

Each module has one clear job. Storage code does not need to know how menus work,
validation does not need to know how CSV files work, and transaction functions can
reuse the same small helpers. This makes each part easier to explain, test, change,
and debug.

The `banking` directory is a custom package. Its `__init__.py` file tells Python that
the directory contains related modules and provides a convenient place to export the
main features. Imports such as `from banking.transactions import deposit` are clear
and avoid putting the entire project in one large file.

## Function-based design

The project deliberately uses functions and simple data structures. A customer is a
dictionary loaded from CSV, and collections of customers and transactions are lists.
This keeps the control flow visible for beginners. OOP is not used for the banking
logic. The required custom exceptions are the sole language-required exception:
Python exception types must inherit from `Exception`.

## Architecture

```text
main.py
   |
   v
customers.py / transactions.py
   |
   +---- validation.py
   +---- utilities.py
   +---- storage.py
   +---- logger.py
   +---- exceptions.py
```

`main.py` handles the user interface. Customer and transaction modules contain the
business operations. Those modules call the supporting validation, utility, storage,
logging, and exception modules.

## Custom exceptions and validation

`BankingError` is the base exception caught by the menu. Its specific child exceptions
describe insufficient funds, invalid amounts, missing accounts, duplicate accounts,
invalid text, and same-account transfers. This produces clearer messages than a
generic error.

Validation cleans account numbers and names before use. Transaction amounts must be
numeric and greater than zero. An initial balance must be numeric and may be zero,
but cannot be negative. Money is calculated with `Decimal` to avoid common floating-
point rounding problems.

## CSV storage

The application uses only standard-library CSV storage. `initialize_files()` creates
missing files and headers automatically. `customers.csv` is rewritten after a balance
change, so balances survive application restarts. `transactions.csv` is append-only
and uses this structure:

```text
transaction_id,date_time,account_number,transaction_type,amount,balance,details,status
```

A successful transfer creates `TRANSFER OUT` for the sender and `TRANSFER IN` for the
receiver. A withdrawal or transfer rejected for insufficient funds creates a `FAILED`
record without changing balances.

## Logging and debugging

Successful operations go to `banking.log`; failures and application errors go to
`error.log`. Each line includes a timestamp and severity. Transaction log messages
also include useful values such as the transaction ID, account, and amount.

For example, after a successful deposit, the CSV contains the new balance and
`banking.log` contains a `Deposit successful` line. If a withdrawal fails, the CSV
contains a `FAILED` entry with the unchanged balance, while `error.log` explains that
the balance was insufficient. Together, the time, transaction ID, input values, and
error reason help a developer reproduce a problem and confirm that no balance was
incorrectly changed.

## Transaction report

Option 7 reads `transactions.csv` and displays:

- total transaction records;
- successful transaction records;
- failed transaction records;
- total successful deposit value;
- total successful withdrawal value; and
- total successful transfer value, counted once using `TRANSFER OUT` records.

## Run the application

Python 3.9 or newer is recommended. No external packages are required.

```powershell
cd D:\julysuper30\banking_app\mini_banking_system
python main.py
```

Example menu:

```text
MINI BANKING SYSTEM
1. Create Account
2. Deposit
3. Withdraw
4. Transfer Money
5. Check Balance
6. Transaction History
7. Generate Transaction Report
8. View Customers
9. Exit
```

## Example usage

Account creation:

```text
Choose an option (1-9): 1
Enter account number: A1001
Enter customer name: Anita Sharma
Enter initial balance: 1000
Account A1001 created successfully.
```

Deposit:

```text
Choose an option (1-9): 2
Enter account number: A1001
Enter deposit amount: 250
Deposit successful. New balance: $1,250.00
```

Withdrawal:

```text
Choose an option (1-9): 3
Enter account number: A1001
Enter withdrawal amount: 100
Withdrawal successful. New balance: $1,150.00
```

Transfer after creating account `A1002`:

```text
Choose an option (1-9): 4
Enter sender account number: A1001
Enter receiver account number: A1002
Enter transfer amount: 300
Transfer successful. Sender balance: $850.00
Receiver balance: $300.00
```

Transaction history:

```text
Choose an option (1-9): 6
Enter account number: A1001
Transaction ID: 9F0C12A5D371
Date/time: 2026-08-11 19:15:00
Type: TRANSFER OUT
Amount: $300.00
Balance: $850.00
Status: SUCCESS
Details: Transferred to A1002
```

Example failed withdrawal:

```text
Choose an option (1-9): 3
Enter account number: A1001
Enter withdrawal amount: 5000
Banking error: Insufficient balance for withdrawal
```

The failed attempt is still written to `transactions.csv` with status `FAILED` and
is explained in `error.log`.

Example report:

```text
TRANSACTION REPORT
-----------------------------------
Total transactions: 5
Successful transactions: 4
Failed transactions: 1
Total deposits: $250.00
Total successful withdrawals: $100.00
Total transfers: $300.00
```
