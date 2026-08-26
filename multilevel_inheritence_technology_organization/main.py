# First level class
class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_person_info(self):
        print("Person Information: \n")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("City: ", self.city)

# Second level class


class Employee(Person):

    def __init__(self, name, age, city, emp_id, salary, company):
        super().__init__(name, age, city)
        self.emp_id = emp_id
        self.salary = salary
        self.company = company

    def get_employee_info(self):
        print("Employee id: ", self.emp_id)
        print("Salary: ", self.salary)
        print("Company: ", self.company)

# Third level class


class Developer(Employee):

    def __init__(self, name, age, city, emp_id, salary, company, language, framework, experience):
        super().__init__(name, age, city, emp_id, salary, company)
        self.language = language
        self.framework = framework
        self.experience = experience

    def get_developer_info(self):
        print("Language: ", self.language)
        print("Framework: ", self.framework)
        print("Experience: ", self.experience)

    def show_complete_info(self):
        print("\n --------------------")
        self.get_person_info()
        self.get_employee_info()
        self.get_developer_info()


# Create 5 Developer objects

developer1 = Developer(
    "Amit",
    28,
    "Delhi",
    "EMP101",
    60000,
    "TechSoft",
    "Python",
    "Django",
    4
)

developer2 = Developer(
    "Rahul",
    30,
    "Mumbai",
    "EMP102",
    75000,
    "CodeTech",
    "JavaScript",
    "React",
    6
)

developer3 = Developer(
    "Priya",
    27,
    "Pune",
    "EMP103",
    65000,
    "WebSoft",
    "PHP",
    "Laravel",
    5
)

developer4 = Developer(
    "Neha",
    25,
    "Bangalore",
    "EMP104",
    55000,
    "AppTech",
    "Python",
    "FastAPI",
    3
)

developer5 = Developer(
    "Vikas",
    32,
    "Kolkata",
    "EMP105",
    85000,
    "CloudSoft",
    "Java",
    "Spring Boot",
    8
)


# Display all developers

developer1.show_complete_info()
developer2.show_complete_info()
developer3.show_complete_info()
developer4.show_complete_info()
developer5.show_complete_info()
