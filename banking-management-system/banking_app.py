"""A small menu-driven banking application using in-memory dictionaries."""

accounts = {}


def read_positive_amount(prompt):
    """Return a positive numeric amount, or None after invalid input."""
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None
    if amount <= 0:
        print("Amount must be positive.")
        return None
    return amount


def read_account_number(prompt="Account number: "):
    account_number = input(prompt).strip()
    if not account_number:
        print("Account number cannot be empty.")
        return None
    return account_number


def create_account():
    account_number = read_account_number()
    if account_number is None:
        return
    if account_number in accounts:
        print("An account with this number already exists.")
        return
    name = input("Customer name: ").strip()
    if not name:
        print("Customer name cannot be empty.")
        return
    initial_balance = read_positive_amount("Initial deposit: ")
    if initial_balance is None:
        return
    accounts[account_number] = {
        "account_number": account_number,
        "name": name,
        "balance": initial_balance,
    }
    print(f"Account {account_number} created successfully.")


def find_account():
    account_number = read_account_number()
    if account_number is None:
        return None
    account = accounts.get(account_number)
    if account is None:
        print("Account not found.")
    return account


def deposit():
    account = find_account()
    if account is None:
        return
    amount = read_positive_amount("Deposit amount: ")
    if amount is None:
        return
    account["balance"] += amount
    print(f"Deposit successful. New balance: {account['balance']:.2f}")


def withdraw():
    account = find_account()
    if account is None:
        return
    amount = read_positive_amount("Withdrawal amount: ")
    if amount is None:
        return
    if amount > account["balance"]:
        print("Insufficient balance. Withdrawal cancelled.")
        return
    account["balance"] -= amount
    print(f"Withdrawal successful. New balance: {account['balance']:.2f}")


def check_balance():
    account = find_account()
    if account is not None:
        print(f"{account['name']}'s balance: {account['balance']:.2f}")


def transfer_money():
    sender_number = read_account_number("From account number: ")
    receiver_number = read_account_number("To account number: ")
    if sender_number is None or receiver_number is None:
        return
    if sender_number == receiver_number:
        print("Transfer accounts must be different.")
        return
    sender = accounts.get(sender_number)
    receiver = accounts.get(receiver_number)
    if sender is None or receiver is None:
        print("Both accounts must exist.")
        return
    amount = read_positive_amount("Transfer amount: ")
    if amount is None:
        return
    if amount > sender["balance"]:
        print("Insufficient balance. Transfer cancelled.")
        return
    sender["balance"] -= amount
    receiver["balance"] += amount
    print(f"Transferred {amount:.2f} from {sender_number} to {receiver_number}.")


def show_all_accounts():
    if not accounts:
        print("No accounts available.")
        return
    print("\nAccount Number | Name | Balance")
    print("-" * 42)
    for account in accounts.values():
        print(f"{account['account_number']} | {account['name']} | {account['balance']:.2f}")
    total_money = sum(account["balance"] for account in accounts.values())
    richest = max(accounts.values(), key=lambda account: account["balance"])
    print("-" * 42)
    print(f"Total money stored in the bank: {total_money:.2f}")
    print(f"Richest customer: {richest['name']} ({richest['balance']:.2f})")


def display_menu():
    print("\n--- Banking Application ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Show All Accounts")
    print("7. Exit")


def main():
    actions = {
        "1": create_account,
        "2": deposit,
        "3": withdraw,
        "4": check_balance,
        "5": transfer_money,
        "6": show_all_accounts,
    }
    while True:
        display_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            print("Thank you for using the banking application.")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option. Please choose a number from 1 to 7.")
        else:
            action()


if __name__ == "__main__":
    main()
