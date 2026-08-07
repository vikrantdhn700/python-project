"""
Student Management System Package (Procedural Version).
"""

from .manager import add_student, remove_student, update_student, search_student, get_all_students
from .exceptions import StudentException

__all__ = [
    "add_student",
    "remove_student",
    "update_student",
    "search_student",
    "get_all_students",
    "StudentException",
]
