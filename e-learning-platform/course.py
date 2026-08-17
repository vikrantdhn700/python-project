"""Course model for the e-learning platform."""


class Course:
    """A course created and taught by an instructor."""

    def __init__(self, course_id: str, title: str, instructor: "Instructor") -> None:
        if not course_id.strip() or not title.strip():
            raise ValueError("Course ID and title cannot be empty.")
        self.course_id = course_id
        self.title = title
        self.instructor = instructor

    def __str__(self) -> str:
        return f"{self.course_id} - {self.title} (Instructor: {self.instructor.name})"


# Imported only for static type checking, preventing a runtime circular import.
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from instructor import Instructor
