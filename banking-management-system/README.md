# Banking Management System

A beginner-friendly, command-line banking application written in Python. It manages bank accounts during a program session and stores every account in dictionaries. It does not require a database or any third-party packages.

## Requirements

- Python 3 installed on the computer
- A terminal opened in this project directory

## Run the Application

Open PowerShell in the project folder and run:

```powershell
python banking_app.py
```

The menu is displayed repeatedly until you select **7. Exit**.

```text
--- Banking Application ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transfer Money
6. Show All Accounts
7. Exit
```

## How Data Is Stored

The program uses one main dictionary named `accounts`. Each key is an account number, and its value is another dictionary containing that account's details.

```python
accounts = {
    "1001": {
        "account_number": "1001",
        "name": "Asha",
        "balance": 1000.0
    }
}
```

Using account numbers as keys makes it quick to find an account and prevents two accounts from using the same number. All records are stored in memory only, so they are cleared when the application exits.

## Menu Options

| Option | What it does |
| --- | --- |
| 1. Create Account | Creates a new account after collecting an account number, customer name, and initial deposit. Duplicate or blank account numbers are rejected. |
| 2. Deposit | Adds a positive amount to an existing account's balance. |
| 3. Withdraw | Removes a positive amount from an existing account only when enough balance is available. |
| 4. Check Balance | Displays the name and current balance for an account. |
| 5. Transfer Money | Moves money from one existing account to another and updates both balances. |
| 6. Show All Accounts | Prints every account, total money held by the bank, and the richest customer. |
| 7. Exit | Closes the application. |

## Business Rules and Validation

The application protects account data with the following checks:

- Account numbers and customer names cannot be empty.
- An account number can be used only once.
- Initial deposits, deposits, withdrawals, and transfers must be greater than zero.
- A withdrawal cannot be larger than the current account balance.
- A transfer requires both source and destination accounts to exist.
- Money cannot be transferred to the same account.
- A transfer is cancelled if the sender does not have enough money.

## Transfer Example

Suppose account `1001` belongs to Asha with a balance of `1000.00`, and account `1002` belongs to Ravi with a balance of `200.00`.

When `300.00` is transferred from `1001` to `1002`:

```text
Asha's balance: 1000.00 -> 700.00
Ravi's balance:  200.00 -> 500.00
```

The total money in the bank stays the same because the amount is removed from one account and added to the other.

## Bank Summary

Choosing **Show All Accounts** prints a table of all accounts. It also calculates:

- **Total money stored in the bank**: the sum of every account balance.
- **Richest customer**: the customer with the highest current balance.

Example:

```text
Account Number | Name | Balance
------------------------------------------
1001 | Asha | 700.00
1002 | Ravi | 500.00
------------------------------------------
Total money stored in the bank: 1200.00
Richest customer: Asha (700.00)
```

## Project Files

| File | Purpose |
| --- | --- |
| `banking_app.py` | Contains the menu, account operations, validation, and program entry point. |
| `README.md` | Explains how to run and use the application. |
