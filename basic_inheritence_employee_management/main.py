
"""Basic employee-management example demonstrating inheritance."""


class Employee:
    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Monthly pay : {self.salary:,.2f}")

    def calculate_salary(self):
        return self.salary * 12


class Developer(Employee):
    def __init__(self, employee_id, name, salary, department,
                 programming_language):
        super().__init__(employee_id, name, salary, department)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, employee_id, name, salary, department, team_size):
        super().__init__(employee_id, name, salary, department)
        self.team_size = team_size


class HR(Employee):
    def __init__(self, employee_id, name, salary, department, region):
        super().__init__(employee_id, name, salary, department)
        self.region = region


def demonstrate_employee(employee):
    employee.display_details()
    print(f"Annual pay  : {employee.calculate_salary():,.2f}")

    if isinstance(employee, Developer):
        print(f"Language    : {employee.programming_language}")
    elif isinstance(employee, Manager):
        print(f"Team size   : {employee.team_size}")
    elif isinstance(employee, HR):
        print(f"Region      : {employee.region}")

    print("-" * 36)


def main():
    employees = [
        Developer(101, "Aarav", 75_000, "Engineering", "Python"),
        Developer(102, "Diya", 80_000, "Engineering", "Java"),
        Manager(201, "Kabir", 110_000, "Management", 8),
        Manager(202, "Meera", 120_000, "Management", 12),
        HR(301, "Rohan", 65_000, "Human Resources", "North"),
        HR(302, "Ananya", 68_000, "Human Resources", "South"),
    ]

    for employee in employees:
        demonstrate_employee(employee)


if __name__ == "__main__":
    main()
