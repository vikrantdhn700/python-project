"""A small student registration system backed by text files."""

import csv
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
STUDENTS_FILE = BASE_DIR / "students.txt"
BACKUP_FILE = BASE_DIR / "students_backup.txt"
NAMES_COURSES_FILE = BASE_DIR / "names_courses.txt"

FIELDS = ("student_id", "name", "email", "phone", "course", "city")

INITIAL_STUDENTS = [
    ("101", "Sudhanshu Kumar", "sudhanshu@example.com",
     "9999999999", "Python", "Bangalore"),
    ("102", "Rahul Sharma", "rahul@example.com",
     "8888888888", "Data Science", "Delhi"),
    ("103", "Priya Nair", "priya@example.com", "9876543210", "Python", "Kochi"),
    ("104", "Amit Patel", "amit@example.com",
     "9123456780", "Web Development", "Ahmedabad"),
    ("105", "Neha Gupta", "neha@example.com",
     "9012345678", "Data Analytics", "Jaipur"),
    ("106", "Arjun Reddy", "arjun@example.com",
     "9988776655", "Machine Learning", "Hyderabad"),
    ("107", "Kavya Iyer", "kavya@example.com", "8877665544", "SQL", "Chennai"),
    ("108", "Rohan Mehta", "rohan@example.com",
     "7766554433", "Cloud Computing", "Pune"),
    ("109", "Ishita Das", "ishita@example.com",
     "9654321098", "Cyber Security", "Kolkata"),
    ("110", "Vikram Singh", "vikram@example.com", "9543210987", "DevOps", "Lucknow"),
]


def write_students(students, file_path=STUDENTS_FILE):
    """Write all student records, replacing the target file."""
    with file_path.open("w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(students)


def append_student(student, file_path=STUDENTS_FILE):
    """Append one student unless its ID already exists."""
    if len(student) != len(FIELDS):
        raise ValueError(
            f"A student record must contain {len(FIELDS)} values.")

    existing_ids = {record[0] for record in read_students(file_path)}
    if student[0] in existing_ids:
        return False

    with file_path.open("a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(student)
    return True


def read_students(file_path=STUDENTS_FILE):
    """Return all complete student records."""
    if not file_path.exists():
        return []
    with file_path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.reader(file))


def read_individual_lines(file_path=STUDENTS_FILE):
    """Print each physical line with its line number."""
    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.rstrip()}")


def count_records(file_path=STUDENTS_FILE):
    """Count student records in a text file."""
    return len(read_students(file_path))


def create_backup(source=STUDENTS_FILE, destination=BACKUP_FILE):
    """Copy the complete student file to a backup file."""
    shutil.copyfile(source, destination)


def export_names_and_courses(destination=NAMES_COURSES_FILE):
    """Write only student names and courses to another text file."""
    with destination.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("name", "course"))
        for record in read_students():
            writer.writerow((record[1], record[4]))


def display_records(records):
    """Display records with their field names."""
    for record in records:
        print(dict(zip(FIELDS, record)))


def main() -> None:
    if not STUDENTS_FILE.exists():
        write_students(INITIAL_STUDENTS)

    new_student = (
        "111",
        "Ananya Verma",
        "ananya@example.com",
        "9432109876",
        "Artificial Intelligence",
        "Mumbai",
    )
    if append_student(new_student):
        print("New student appended successfully.\n")
    else:
        print("Student 111 already exists; duplicate was not added.\n")

    print("Complete student records:")
    display_records(read_students())

    print("\nIndividual lines:")
    read_individual_lines()

    print(f"\nTotal student records: {count_records()}")

    create_backup()
    export_names_and_courses()
    print(f"Backup created: {BACKUP_FILE.name}")
    print(f"Names and courses exported: {NAMES_COURSES_FILE.name}")


if __name__ == "__main__":
    main()
