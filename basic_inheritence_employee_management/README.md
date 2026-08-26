# Employee Management System Using Inheritance

This is a simple Python console project that demonstrates object-oriented
inheritance through an employee management system.

## What Is Inheritance?

Inheritance allows one class to receive properties and methods from another
class. The class providing the shared features is called the **parent class**,
and the classes receiving those features are called **child classes**.

Inheritance is useful because it:

- Reduces repeated code
- Places shared behavior in one class
- Makes programs easier to maintain
- Allows child classes to add their own specialized features

## Class Structure

### Parent Class: `Employee`

Every employee has these shared properties:

- `employee_id`
- `name`
- `salary`
- `department`

The parent class also provides these shared methods:

- `display_details()` displays the employee's information.
- `calculate_salary()` calculates the annual salary from the monthly salary.

### Child Class: `Developer`

`Developer` inherits all properties and methods from `Employee` and adds:

- `programming_language`

### Child Class: `Manager`

`Manager` inherits all properties and methods from `Employee` and adds:

- `team_size`

### Child Class: `HR`

`HR` inherits all properties and methods from `Employee` and adds:

- `region`

## How Inheritance Is Used

Each child class declares `Employee` as its parent:

```python
class Developer(Employee):
    pass
```

The child constructors use `super()` to initialize the inherited employee
properties:

```python
super().__init__(employee_id, name, salary, department)
```

As a result, methods such as `display_details()` and `calculate_salary()` are
written once in `Employee` and reused by all three child classes.

## Objects Created

The program creates six objects in total:

- Two `Developer` objects
- Two `Manager` objects
- Two `HR` objects

Each object demonstrates inherited properties, inherited methods, and its own
child-specific attribute.

## Requirements

- Python 3.8 or later
- No external packages are required

## Run the Project

Open a terminal in the project directory and run:

```powershell
python main.py
```

The program prints each employee's details, annual salary, and child-specific
information.

## Suggested Video Explanation

During the video demonstration, explain:

1. Inheritance means that child classes receive features from a parent class.
2. `Employee` is the parent class because it contains shared employee data and
   behavior.
3. `Developer`, `Manager`, and `HR` are child classes because they inherit from
   `Employee`.
4. `super().__init__()` initializes the properties defined by the parent class.
5. Every child object can call the inherited `display_details()` and
   `calculate_salary()` methods.
6. Each child class adds a specialized attribute for its role.
7. Inheritance improves code reusability because the shared properties and
   methods are defined only once.

## Project Files

```text
basic_inheritence_employee_management/
|-- main.py
`-- README.md
```
