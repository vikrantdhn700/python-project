# Banking System Using Hierarchical Inheritance

This Python project demonstrates **hierarchical inheritance** through a simple
banking system. One parent class provides common account functionality, while
three child classes represent different account types.

## Class Structure

```text
                    BankAccount
                         |
          +--------------+---------------+
          |              |               |
  SavingsAccount   CurrentAccount   SalaryAccount
```

In hierarchical inheritance, multiple child classes inherit from the same
parent class. Here, `SavingsAccount`, `CurrentAccount`, and `SalaryAccount` all
inherit from `BankAccount`.

## Parent Class: BankAccount

The `BankAccount` class contains information and behavior shared by every bank
account.

### Attributes

- `account_number`
- `holder_name`
- `balance`

### Methods

- `deposit(amount)` — adds a valid amount to the balance
- `display_balance()` — displays the available account balance
- `account_details()` — displays the account number, holder, and balance

The constructor rejects a negative opening balance, and `deposit()` accepts only
amounts greater than zero.

## Child Classes

### SavingsAccount

Adds an `interest_rate` property.

### CurrentAccount

Adds an `overdraft_limit` property.

### SalaryAccount

Adds the following properties:

- `employer`
- `monthly_salary`

Each child class extends `account_details()`. It first calls the parent version
with `super().account_details()` and then displays its account-specific details.

## Inherited Behavior

All child objects inherit `deposit()` and `display_balance()` from
`BankAccount`. Therefore, the same operations work on savings, current, and
salary accounts without duplicating their implementation.

The project creates six objects—two objects for each account type—and
demonstrates:

1. Displaying common and account-specific details
2. Depositing ₹5,000 into each account
3. Displaying the updated balance

## Run the Program

Open a terminal in the project directory and run:

```bash
python main.py
```

## Project Structure

```text
heirerical_inheritence_banking_sys/
|-- main.py
`-- README.md
```
