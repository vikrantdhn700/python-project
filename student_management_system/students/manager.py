from .logger import log_message
from . import storage
from .exceptions import StudentException

def add_student(student_id: str, name: str, age: int, course: str) -> None:
    students = storage.load_data()
    if student_id in students:
        log_message(f"Student '{name}' (ID: {student_id}) already exists.", "error")
        raise StudentException(f"Student ID '{student_id}' already exists.")
    
    students[student_id] = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    storage.save_students(students)
    log_message(f"Added Student: ID={student_id}, Name={name}", "info")

def remove_student(student_id: str):
    students = storage.load_data()
    if student_id in students:
        removed_student = students.pop(student_id)
    else:
        log_message(f"Failed Remove: ID {student_id} not found.", "error")
        raise StudentException(f"Student ID '{student_id}' not found.")
        
    storage.save_students(students)
    log_message(f"Removed Student: ID={student_id}", "info")
    return removed_student

def update_student(student_id: str, name: str , age: int, course: str) -> None:
    students = storage.load_data()
    if student_id not in students:
        log_message(f"Failed Update: Student ID {student_id} not found.", "error")
        raise StudentException(f"Student ID '{student_id}' not found.")

    student = students[student_id]

    if name is not None:
        student["name"] = name
    if age is not None:
        student["age"] = age
    if course is not None:
        student["course"] = course

    storage.save_students(students)
    log_message(f"Updated Student: ID={student_id}", "info")

def search_student(student_id: str):
    students = storage.load_data()
    if student_id not in students:
        log_message(f"Failed Search: Student ID {student_id} not found.", "error")
        raise StudentException(f"Student ID '{student_id}' not found.")
    
    log_message(f"Searched Student: ID={student_id}", "info")  
    return students[student_id]

def get_all_students():
    students = storage.load_data()
    log_message("Retrieved all students", "info")
    return list(students.values())