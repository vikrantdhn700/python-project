"""Main entry point for the Employee Payroll Calculator."""

from payroll.exceptions import PayrollError
from payroll.employees import (
    add_employee_interactive,
    calculate_salary_interactive,
    calculate_tax_interactive,
    calculate_bonus_interactive,
    generate_payslip_interactive,
    display_employees,
)
from payroll.logger import log_error


def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 40)
    print("       EMPLOYEE PAYROLL CALCULATOR")
    print("=" * 40)

    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Calculate Tax")
    print("4. Calculate Bonus")
    print("5. Generate Payslip")
    print("6. View Employees")
    print("7. Exit")

    print("=" * 40)


def main():
    """Run the Employee Payroll Calculator."""

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                add_employee_interactive()

            elif choice == "2":
                calculate_salary_interactive()

            elif choice == "3":
                calculate_tax_interactive()

            elif choice == "4":
                calculate_bonus_interactive()

            elif choice == "5":
                generate_payslip_interactive()

            elif choice == "6":
                display_employees()

            elif choice == "7":
                print("Exiting Payroll Calculator. Goodbye!")
                break

            else:
                raise PayrollError(
                    "Invalid choice. Please enter a number from 1 to 7."
                )

        except (ValueError, TypeError) as error:

            log_error(f"Invalid input: {error}")

            print("Error: Invalid input. Please try again.")

        except PayrollError as error:

            log_error(f"Unexpected error: {error}")

            print(f"Error: An unexpected error occurred. {error}")


if __name__ == "__main__":
    main()
