# Multilevel Inheritance: Technology Organization

A simple Python project that demonstrates **multilevel inheritance** using roles in a technology organization.

## Inheritance Structure

```text
Person
  -> Employee
       -> Developer
```

- `Person` stores personal details: name, age, and city.
- `Employee` inherits from `Person` and adds employee ID, salary, and company.
- `Developer` inherits from `Employee` and adds programming language, framework, and experience.

The `Developer.show_complete_info()` method uses methods inherited from all three levels to display a developer's complete details.

## Requirements

- Python 3.x
- No third-party packages are required.

## Run the Project

Open a terminal in the project directory and run:

```bash
python main.py
```

On systems where Python 3 uses a separate command, run:

```bash
python3 main.py
```

## Example Output

The program creates five `Developer` objects and prints information similar to:

```text
--------------------
Person Information:

Name:  Amit
Age:  28
City:  Delhi
Employee id:  EMP101
Salary:  60000
Company:  TechSoft
Language:  Python
Framework:  Django
Experience:  4
```

## Project Structure

```text
multilevel_inheritence_technology_organization/
|-- main.py
`-- README.md
```

## Concepts Demonstrated

- Classes and objects
- Multilevel inheritance
- Constructor chaining with `super()`
- Method reuse across parent and child classes
- Instance attributes
