# E-Learning Platform Using Python OOP

## Project Overview

This project is a small console-based E-Learning Platform created with Python.
Its main purpose is to demonstrate object-oriented programming (OOP), especially
classes, objects, inheritance, encapsulation, method reuse, relationships between
objects, input validation, and type hints.

The platform contains two kinds of users:

- A **student** can enroll in courses, view enrolled courses, update course
  progress, and check progress.
- An **instructor** can create courses and display all the courses they teach.

Both students and instructors share common details such as a user ID, name, and
email address. Instead of defining these details twice, the project places them
in a parent `User` class. The `Student` and `Instructor` classes inherit this
common data and behavior from `User`.

The demonstration creates two students, two instructors, and three courses. It
then assigns courses to instructors, enrolls students, updates their progress,
and displays the final information.

## Project Structure

```text
e-learning-platform/
|-- user.py          # Parent User class
|-- student.py       # Student child class
|-- instructor.py    # Instructor child class
|-- course.py        # Course class
|-- main.py          # Creates objects and runs the demonstration
`-- README.md        # Project documentation
```

## OOP Design

The inheritance hierarchy used by the project is:

```text
                 User
                /    \
         Student      Instructor
```

`User` is the parent or base class. `Student` and `Instructor` are child or
derived classes. Because both child classes inherit from `User`, every student
and instructor automatically has the `user_id`, `name`, and `email` attributes,
as well as the `display_profile()` method.

The `Course` class is not a child of `User`. Instead, it has an association with
`Instructor`: every course stores the instructor who teaches it. A student also
has an association with courses through the student's enrollment dictionary.

## Detailed File Explanation

### `user.py`

This file defines the parent `User` class. It holds the information and behavior
that are common to every platform user.

#### `User.__init__(user_id, name, email)`

The constructor initializes three instance attributes:

- `user_id`: A positive integer that uniquely identifies the user.
- `name`: The user's full name.
- `email`: The user's email address.

The constructor also validates its input. It raises `ValueError` when the user ID
is zero or negative, the name is empty, or the email does not contain an `@`
symbol. Centralizing this validation in `User` means both child classes use the
same rules without duplicating code.

#### `User.display_profile()`

This method displays the user's ID, name, and email on one line. The method is
inherited by both `Student` and `Instructor`. Neither child class needs to define
its own copy of this method.

### `student.py`

This file defines `Student`, a child class declared as `class Student(User)`.
That declaration establishes inheritance from the `User` parent class.

#### `Student.__init__(user_id, name, email)`

The constructor calls `super().__init__(user_id, name, email)`. The `super()`
call runs the parent constructor, which creates and validates the common user
attributes. The student constructor then creates `_enrollments`, a private-by-
convention dictionary used to store courses and progress percentages.

Each dictionary entry uses:

- A `Course` object as its key.
- An integer from `0` to `100` as its value.

This structure allows one collection to record both which courses the student
has joined and how much of each course the student has completed.

#### `Student.enroll(course)`

This method enrolls the student in a `Course` object. A new enrollment begins at
`0%` progress. If the student is already enrolled, the method displays a message
and does not create a duplicate enrollment.

#### `Student.update_progress(course, progress)`

This method changes the student's completion percentage for a course. It checks
that the student is already enrolled and that the supplied percentage is between
`0` and `100`. Invalid operations raise `ValueError` with a useful message.

#### `Student.view_enrolled_courses()`

This method displays every course in which the student is enrolled. Printing a
course automatically uses `Course.__str__()`, so each line includes the course
ID, title, and instructor name. If the student has no enrollments, an explanatory
message is displayed.

#### `Student.check_course_progress()`

This method displays the course title and completion percentage for every
enrollment. It also handles the case in which the student has no courses.

### `instructor.py`

This file defines `Instructor`, another child class declared as
`class Instructor(User)`. It inherits the common attributes and profile method
from `User` but adds behavior specifically needed by instructors.

#### `Instructor.__init__(user_id, name, email)`

Like `Student`, this constructor uses `super().__init__()` to initialize the
inherited user details. It then creates `_courses`, a private-by-convention list
containing the `Course` objects created by the instructor.

#### `Instructor.create_course(course_id, title)`

This method creates a new `Course`. It passes `self` to the course constructor,
which records the current instructor as the teacher. The new course is added to
the instructor's `_courses` list and returned to the caller. Returning the object
allows the main program to enroll students in that course.

#### `Instructor.display_teaching_courses()`

This method displays the ID and title of every course taught by the instructor.
If no courses have been created, it displays a suitable empty-state message.

### `course.py`

This file defines the `Course` class. A course is a separate domain object rather
than a subclass of `User` because a course is not a type of user.

#### `Course.__init__(course_id, title, instructor)`

The constructor stores:

- `course_id`: A short course identifier such as `CS101`.
- `title`: A readable course title such as `Python Programming`.
- `instructor`: The `Instructor` object responsible for the course.

The constructor rejects an empty course ID or title. The instructor parameter is
annotated as `"Instructor"`, which is a forward reference because the two classes
refer to each other.

At the bottom of the file, `TYPE_CHECKING` is used to import `Instructor` only
when a static type checker is analyzing the program. This avoids a circular
runtime import: `instructor.py` imports `Course`, while `Course` needs the
`Instructor` name only for its type annotation.

#### `Course.__str__()`

This special method controls how a course appears when passed to `print()` or
converted to a string. It returns the course ID, title, and instructor name in a
readable format.

### `main.py`

This is the entry point and demonstration file. It imports `Instructor`,
`Student`, and `User`, creates all sample objects, and calls their methods.

The `main()` function performs the following operations:

1. Creates two instructors: Dr. Ananya Rao and Prof. Rahul Mehta.
2. Creates two students: Aarav Sharma and Meera Patel.
3. Creates three courses through the instructors' `create_course()` method.
4. Calls the inherited `display_profile()` method for all four users.
5. Uses `isinstance()` to prove that a `Student` and an `Instructor` are both
   instances of the parent `User` type.
6. Displays the courses taught by each instructor.
7. Enrolls each student in two courses.
8. Updates each student's course progress.
9. Displays every student's enrolled courses and progress percentages.

The final `if __name__ == "__main__":` condition runs `main()` only when the file
is executed directly. It prevents the demonstration from running automatically
if `main.py` is imported by another Python program.

## How Inheritance Is Demonstrated

Inheritance is visible in both the class definitions and the program output:

```python
class Student(User):
    ...

class Instructor(User):
    ...
```

The constructors reuse the parent's initialization logic:

```python
super().__init__(user_id, name, email)
```

The main program calls `display_profile()` on student and instructor objects even
though that method exists only in `User`. It also verifies the relationship at
runtime:

```python
isinstance(student_one, User)       # True
isinstance(instructor_one, User)    # True
```

This design avoids repeated code and makes it easier to add another kind of user,
such as an administrator, in the future.

## Requirements

- Python 3.9 or newer is recommended because the project uses built-in generic
  type hints such as `list[Course]` and `dict[Course, int]`.
- No external libraries or package installation are required.

## How to Run

Open PowerShell or another terminal, move to the project directory, and run:

```powershell
cd D:\julysuper30\e-learning-platform
python main.py
```

If Python cannot write bytecode cache files because of folder permissions, run:

```powershell
python -B main.py
```

The `-B` option disables creation of the `__pycache__` directory and does not
change the program's behavior.

## Expected Demonstration Results

When the program runs, it displays:

- Profiles for two instructors and two students.
- `True` for both inheritance checks.
- Two courses taught by Dr. Ananya Rao.
- One course taught by Prof. Rahul Mehta.
- Two enrollments for Aarav Sharma.
- Two enrollments for Meera Patel.
- Progress values of `75%`, `40%`, `60%`, and `85%` for the corresponding
  student-course combinations.

## Validation and Error Handling

The project includes basic safeguards to keep its objects in a valid state:

- User IDs must be positive.
- Names cannot be empty.
- Email addresses must contain `@`.
- Course IDs and titles cannot be empty.
- Duplicate course enrollment is prevented.
- Progress cannot be updated before enrollment.
- Course progress must remain between `0` and `100`.

These checks demonstrate that classes can protect their own data instead of
depending on the main program to validate every operation.
