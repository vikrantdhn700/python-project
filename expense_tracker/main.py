""" This is the main application file for the Personal Expense Tracker."""

from expense_manager.expenses import (
    add_expense,
    delete_expense,
    update_expense,
    load_expenses
)

from expense_manager.validation import (
    validate_date,
    validate_amount,
    validate_category,
    validate_description,
    validate_expense_id,
    validate_month
)

from expense_manager.reports import (
    monthly_summary,
    category_summary,
    highest_expense,
    export_report
)

from expense_manager.logger import (
    log_info,
    log_error,
    log_warning
)


def display_expenses(expenses):
    """Display expenses in formatted form."""

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 80)
    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':<10}"
    )
    print("=" * 80)

    for expense in expenses:

        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{float(expense['amount']):<9.2f}"
        )

    print("=" * 80)


def add_expense_menu():
    """Menu for adding an expense."""

    try:
        date = input(
            "Enter date (YYYY-MM-DD): "
        )

        validate_date(date)

        category = input(
            "Enter category: "
        )

        category = validate_category(category)

        description = input(
            "Enter description: "
        )

        description = validate_description(description)

        amount = input(
            "Enter amount: "
        )

        amount = validate_amount(amount)

        expense = add_expense(
            date,
            category,
            description,
            amount
        )

        log_info(
            f"Expense added successfully. ID={expense['id']}"
        )

        print("\nExpense added successfully.")
        print(f"Expense ID: {expense['id']}")

    except ValueError as e:

        log_error(f"Add expense validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:
        log_error(f"Add expense error: {e}")
        print(f"\nError: {e}")


def delete_expense_menu():
    """Menu for deleting an expense."""

    try:
        expense_id = input(
            "Enter expense ID to delete: "
        )

        expense_id = validate_expense_id(expense_id)

        success = delete_expense(expense_id)

        if success:

            log_info(
                f"Expense deleted successfully. ID={expense_id}"
            )

            print("\nExpense deleted successfully.")

        else:

            log_warning(
                f"Expense not found. ID={expense_id}"
            )

            print("\nExpense not found.")

    except ValueError as e:

        log_error(f"Delete validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:

        log_error(f"Delete expense error: {e}")
        print(f"\nError: {e}")


def update_expense_menu():
    """Menu for updating an expense."""

    try:
        expense_id = input(
            "Enter expense ID to update: "
        )

        expense_id = validate_expense_id(expense_id)

        date = input(
            "Enter new date (YYYY-MM-DD): "
        )

        validate_date(date)

        category = input(
            "Enter new category: "
        )

        category = validate_category(category)

        description = input(
            "Enter new description: "
        )

        description = validate_description(description)

        amount = input(
            "Enter new amount: "
        )

        amount = validate_amount(amount)

        success = update_expense(
            expense_id,
            date,
            category,
            description,
            amount
        )

        if success:

            log_info(
                f"Expense updated successfully. ID={expense_id}"
            )

            print("\nExpense updated successfully.")

        else:

            log_warning(
                f"Expense not found for update. ID={expense_id}"
            )

            print("\nExpense not found.")

    except ValueError as e:

        log_error(f"Update validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:

        log_error(f"Update expense error: {e}")
        print(f"\nError: {e}")


def monthly_summary_menu():
    """Display monthly expense summary."""

    try:
        month = input(
            "Enter month (YYYY-MM): "
        )

        validate_month(month)

        expenses, total = monthly_summary(month)

        print(f"\nMONTHLY SUMMARY - {month}")
        print("-" * 40)

        print(f"Number of expenses: {len(expenses)}")
        print(f"Total expense: ₹{total:.2f}")

        display_expenses(expenses)

        log_info(
            f"Monthly summary generated for {month}"
        )

    except ValueError as e:

        log_error(f"Monthly summary validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:

        log_error(f"Monthly summary error: {e}")
        print(f"\nError: {e}")


def category_summary_menu():
    """Display category-wise summary."""

    try:
        month = input(
            "Enter month (YYYY-MM) or press Enter for all: "
        )

        if month:
            validate_month(month)

        summary = category_summary(
            month if month else None
        )

        if not summary:

            print("\nNo expenses found.")
            return

        print("\nCATEGORY-WISE SUMMARY")
        print("-" * 40)

        for category, amount in summary.items():

            print(
                f"{category:<20} ₹{amount:.2f}"
            )

        log_info(
            "Category-wise summary generated."
        )

    except ValueError as e:

        log_error(f"Category summary validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:

        log_error(f"Category summary error: {e}")
        print(f"\nError: {e}")


def highest_expense_menu():
    """Display highest expense."""

    try:
        month = input(
            "Enter month (YYYY-MM) or press Enter for all: "
        )

        if month:
            validate_month(month)

        expense = highest_expense(
            month if month else None
        )

        if expense is None:

            print("\nNo expenses found.")
            return

        print("\nHIGHEST EXPENSE")
        print("-" * 40)

        print(f"ID: {expense['id']}")
        print(f"Date: {expense['date']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ₹{float(expense['amount']):.2f}")

        log_info(
            "Highest expense displayed."
        )

    except ValueError as e:

        log_error(f"Highest expense validation error: {e}")
        print(f"\nError: {e}")

    except OSError as e:

        log_error(f"Highest expense error: {e}")
        print(f"\nError: {e}")


def view_all_expenses():
    """Display all expenses."""

    try:
        expenses = load_expenses()

        display_expenses(expenses)

        log_info("All expenses displayed.")

    except OSError as e:

        log_error(f"View expenses error: {e}")
        print(f"\nError: {e}")


def export_report_menu():
    """Export monthly report."""

    try:
        month = input(
            "Enter month (YYYY-MM): "
        )

        validate_month(month)

        filename = export_report(month)

        log_info(f"Monthly report exported: {filename}")

        print("\nReport generated successfully.")

        print(f"File: {filename}")

    except ValueError as e:

        log_error(f"Report validation error: {e}")
        print(f"Error: {e}")

    except OSError as e:

        log_error(f"Report export error: {e}")
        print(f"\nError: {e}")


def show_menu():
    """Display application menu."""

    print("\n")
    print("=" * 50)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 50)

    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. View All Expenses")
    print("5. Monthly Summary")
    print("6. Category-wise Summary")
    print("7. Highest Expense")
    print("8. Export Monthly Report")
    print("9. Exit")

    print("=" * 50)


def main():
    """Main application function."""

    log_info("Expense Tracker application started.")

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":
                add_expense_menu()

            elif choice == "2":
                delete_expense_menu()

            elif choice == "3":
                update_expense_menu()

            elif choice == "4":
                view_all_expenses()

            elif choice == "5":
                monthly_summary_menu()

            elif choice == "6":
                category_summary_menu()

            elif choice == "7":
                highest_expense_menu()

            elif choice == "8":
                export_report_menu()

            elif choice == "9":

                log_info("Expense Tracker application stopped.")

                print("\nThank you for using Expense Tracker.")
                break

            else:

                log_warning(f"Invalid menu choice: {choice}")

                print("\nInvalid choice. Please select 1-9.")

        except OSError as e:

            log_error(f"Unexpected application error: {e}")

            print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
