"""Employee and payroll management functions."""

from .calculations import (
    calculate_bonus,
    calculate_gross_salary,
    calculate_net_salary,
    calculate_tax,
)

from .exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
)

from .logger import log_payroll

from .storage import (
    load_employees,
    save_employees,
    save_payroll_record,
)

from .validators import (
    validate_bonus_percentage,
    validate_department,
    validate_employee_id,
    validate_month,
    validate_name,
    validate_salary,
)


def add_employee(
    employee_id,
    name,
    department,
    monthly_salary,
    bonus_percentage
):
    """Add a new employee."""

    employee_id = validate_employee_id(
        employee_id
    )

    name = validate_name(name)

    department = validate_department(
        department
    )

    monthly_salary = validate_salary(
        monthly_salary
    )

    bonus_percentage = validate_bonus_percentage(
        bonus_percentage
    )

    employees = load_employees()

    for employee in employees:

        if employee["employee_id"] == employee_id:

            raise DuplicateEmployeeError(
                f"Employee '{employee_id}' already exists."
            )

    new_employee = {

        "employee_id": employee_id,

        "name": name,

        "department": department,

        "monthly_salary":
            f"{monthly_salary:.2f}",

        "bonus_percentage":
            f"{bonus_percentage:.2f}",
    }

    employees.append(new_employee)

    save_employees(employees)

    log_payroll(
        f"Employee added: "
        f"{employee_id} - {name}"
    )

    return new_employee


def find_employee(employee_id):
    """Find employee by employee ID."""

    employee_id = validate_employee_id(
        employee_id
    )

    employees = load_employees()

    for employee in employees:

        if employee["employee_id"] == employee_id:

            return employee

    raise EmployeeNotFoundError(
        f"Employee '{employee_id}' was not found."
    )


def calculate_employee_salary(employee_id):
    """Calculate complete salary information."""

    employee = find_employee(
        employee_id
    )

    salary = validate_salary(
        employee["monthly_salary"]
    )

    bonus_percentage = validate_bonus_percentage(
        employee["bonus_percentage"]
    )

    bonus = calculate_bonus(
        salary,
        bonus_percentage
    )

    gross_salary = calculate_gross_salary(
        salary,
        bonus
    )

    tax = calculate_tax(
        gross_salary
    )

    net_salary = calculate_net_salary(
        salary,
        bonus,
        tax
    )

    log_payroll(
        f"Salary calculated: "
        f"{employee_id}, "
        f"net salary={net_salary:.2f}"
    )

    return {

        "employee": employee,

        "bonus": bonus,

        "gross_salary":
            gross_salary,

        "tax":
            tax,

        "net_salary":
            net_salary,
    }


def calculate_employee_tax(employee_id):
    """Calculate employee tax."""

    result = calculate_employee_salary(
        employee_id
    )

    tax = result["tax"]

    log_payroll(
        f"Tax calculated: "
        f"{employee_id}, "
        f"tax={tax:.2f}"
    )

    return tax


def calculate_employee_bonus(employee_id):
    """Calculate employee bonus."""

    employee = find_employee(
        employee_id
    )

    salary = validate_salary(
        employee["monthly_salary"]
    )

    bonus_percentage = validate_bonus_percentage(
        employee["bonus_percentage"]
    )

    bonus = calculate_bonus(
        salary,
        bonus_percentage
    )

    log_payroll(
        f"Bonus calculated: "
        f"{employee_id}, "
        f"bonus={bonus:.2f}"
    )

    return bonus


def generate_payslip(
    employee_id,
    month
):
    """Generate and store employee payslip."""

    month = validate_month(
        month
    )

    result = calculate_employee_salary(
        employee_id
    )

    employee = result["employee"]

    record = {

        "employee_id":
            employee["employee_id"],

        "employee_name":
            employee["name"],

        "month":
            month,

        "gross_salary":
            f"{result['gross_salary']:.2f}",

        "tax":
            f"{result['tax']:.2f}",

        "bonus":
            f"{result['bonus']:.2f}",

        "net_salary":
            f"{result['net_salary']:.2f}",
    }

    save_payroll_record(
        record
    )

    log_payroll(
        f"Payslip generated: "
        f"{employee_id}, "
        f"month={month}"
    )

    return record


def add_employee_interactive():
    """Interactive Add Employee operation."""

    print("\nAdd Employee")
    print("-" * 25)

    employee_id = input(
        "Employee ID: "
    )

    name = input(
        "Employee Name: "
    )

    department = input(
        "Department: "
    )

    salary = input(
        "Monthly Salary: "
    )

    bonus = input(
        "Bonus Percentage: "
    )

    employee = add_employee(
        employee_id,
        name,
        department,
        salary,
        bonus
    )

    print(
        f"\nEmployee "
        f"'{employee['name']}' "
        "added successfully."
    )


def calculate_salary_interactive():
    """Interactive salary calculation."""

    employee_id = input(
        "Enter Employee ID: "
    )

    result = calculate_employee_salary(
        employee_id
    )

    employee = result["employee"]

    print("\nSalary Details")
    print("-" * 35)

    print(
        f"Employee     : "
        f"{employee['name']}"
    )

    print(
        f"Basic Salary : "
        f"{float(employee['monthly_salary']):.2f}"
    )

    print(
        f"Bonus        : "
        f"{result['bonus']:.2f}"
    )

    print(
        f"Gross Salary : "
        f"{result['gross_salary']:.2f}"
    )

    print(
        f"Tax          : "
        f"{result['tax']:.2f}"
    )

    print(
        f"Net Salary   : "
        f"{result['net_salary']:.2f}"
    )


def calculate_tax_interactive():
    """Interactive tax calculation."""

    employee_id = input(
        "Enter Employee ID: "
    )

    tax = calculate_employee_tax(
        employee_id
    )

    print(
        f"Tax: {tax:.2f}"
    )


def calculate_bonus_interactive():
    """Interactive bonus calculation."""

    employee_id = input(
        "Enter Employee ID: "
    )

    bonus = calculate_employee_bonus(
        employee_id
    )

    print(
        f"Bonus: {bonus:.2f}"
    )


def generate_payslip_interactive():
    """Interactive payslip generation."""

    employee_id = input(
        "Enter Employee ID: "
    )

    month = input(
        "Enter Payroll Month: "
    )

    record = generate_payslip(
        employee_id,
        month
    )

    print("\n" + "=" * 45)

    print(
        "              PAYSLIP"
    )

    print("=" * 45)

    print(
        f"Employee ID : "
        f"{record['employee_id']}"
    )

    print(
        f"Employee    : "
        f"{record['employee_name']}"
    )

    print(
        f"Month       : "
        f"{record['month']}"
    )

    print("-" * 45)

    print(
        f"Gross Salary: "
        f"{float(record['gross_salary']):.2f}"
    )

    print(
        f"Bonus       : "
        f"{float(record['bonus']):.2f}"
    )

    print(
        f"Tax         : "
        f"{float(record['tax']):.2f}"
    )

    print(
        f"Net Salary  : "
        f"{float(record['net_salary']):.2f}"
    )

    print("=" * 45)


def display_employees():
    """Display all employees."""

    employees = load_employees()

    if not employees:

        print(
            "No employees found."
        )

        return

    print("\nEmployee List")

    print("-" * 80)

    print(
        f"{'ID':<12}"
        f"{'Name':<20}"
        f"{'Department':<20}"
        f"{'Salary':>15}"
    )

    print("-" * 80)

    for employee in employees:

        print(
            f"{employee['employee_id']:<12}"
            f"{employee['name']:<20}"
            f"{employee['department']:<20}"
            f"{float(employee['monthly_salary']):>15.2f}"
        )

    print("-" * 80)
