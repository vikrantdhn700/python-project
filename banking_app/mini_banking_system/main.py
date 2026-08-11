"""Command-line entry point for the Mini Banking System."""

from banking.customers import (
    check_balance_interactive,
    create_account_interactive,
    display_customers,
)
from banking.exceptions import BankingError
from banking.logger import initialize_logs, log_error
from banking.storage import initialize_files
from banking.transactions import (
    deposit_interactive,
    generate_report_interactive,
    transaction_history_interactive,
    transfer_interactive,
    withdraw_interactive,
)


def display_menu():
    """Print the available application actions."""
    print("\nMINI BANKING SYSTEM")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Generate Transaction Report")
    print("8. View Customers")
    print("9. Exit")


def run_application():
    """Initialize storage and process menu choices until the user exits."""
    initialize_files()
    initialize_logs()
    actions = {
        "1": create_account_interactive,
        "2": deposit_interactive,
        "3": withdraw_interactive,
        "4": transfer_interactive,
        "5": check_balance_interactive,
        "6": transaction_history_interactive,
        "7": generate_report_interactive,
        "8": display_customers,
    }

    while True:
        display_menu()
        choice = input("Choose an option (1-9): ").strip()
        if choice == "9":
            print("Thank you for using the Mini Banking System.")
            break
        if choice not in actions:
            message = f"Invalid menu option: {choice}"
            log_error(message)
            print("Invalid option. Please choose a number from 1 to 9.")
            continue
        try:
            actions[choice]()
        except BankingError as error:
            log_error(f"Handled banking error: {error}")
            print(f"Banking error: {error}")
        except Exception as error:
            log_error(f"Unexpected application error: {type(error).__name__}: {error}")
            print("An unexpected error occurred. See error.log for details.")


if __name__ == "__main__":
    run_application()
