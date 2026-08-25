# Student Registration System Using Text Files

A small Python application that manages student registration records using plain text files. It demonstrates writing, appending, reading, counting, backing up, and extracting selected student data without requiring a database.

## Features

The application can:

- Write a collection of student records to a text file
- Append a new student record
- Prevent duplicate student IDs from being appended
- Read and display all student records
- Read and display individual numbered lines
- Count the total number of student records
- Copy all records into a backup file
- Export only student names and courses to another file
- Recreate the initial dataset if `students.txt` is missing

## Project Structure

```text
student_registration_system_using_txtfile/
|-- main.py
|-- students.txt
|-- students_backup.txt
|-- names_courses.txt
`-- readme.md
```

## Student Record Format

Each student record contains six comma-separated fields:

| Field | Description |
|---|---|
| `student_id` | Unique student identifier |
| `name` | Student's full name |
| `email` | Student's email address |
| `phone` | Student's phone number |
| `course` | Registered course |
| `city` | Student's city |

Example:

```text
101,Sudhanshu Kumar,sudhanshu@example.com,9999999999,Python,Bangalore
```

The included dataset currently contains 11 student records.

## Requirements

- Python 3.8 or later

The project uses only Python standard-library modules (`csv`, `shutil`, and `pathlib`), so no external packages are required.

## Running the Application

Open a terminal in the project directory and run:

```bash
python main.py
```

The program will:

1. Create the initial student file if it does not exist.
2. Attempt to append the demonstration student with ID `111`.
3. Skip the append if that ID already exists.
4. Display all parsed student records.
5. Display every text-file line with its line number.
6. Print the total record count.
7. Create or refresh the backup file.
8. Create or refresh the names-and-courses file.

The script uses paths based on the location of `main.py`, so it can be launched from another working directory.

## Output Files

### `students.txt`

Stores the complete student records as comma-separated text.

### `students_backup.txt`

Contains an exact copy of `students.txt`. It is replaced with the latest source data each time the program runs.

### `names_courses.txt`

Contains only the `name` and `course` fields and includes a header row:

```text
name,course
Sudhanshu Kumar,Python
Rahul Sharma,Data Science
```

## Main Functions

| Function | Purpose |
|---|---|
| `write_students()` | Replaces a file with the supplied student records |
| `append_student()` | Appends one record if its student ID is unique |
| `read_students()` | Parses and returns all student records |
| `read_individual_lines()` | Prints each raw line with its line number |
| `count_records()` | Returns the number of stored records |
| `create_backup()` | Copies the student data to the backup file |
| `export_names_and_courses()` | Writes student names and courses to a separate file |
| `display_records()` | Displays parsed records with field labels |

## Notes

- Student IDs must be unique.
- Each record must contain exactly six values.
- Phone numbers are stored as text so their digits remain unchanged.
- Running the program repeatedly does not duplicate student ID `111`.
- The backup and names/course export are regenerated whenever the program runs.
