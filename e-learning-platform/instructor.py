"""Instructor model inherited from User."""

from course import Course
from user import User


class Instructor(User):
    """A user who can create and teach courses."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id, name, email)
        self._courses: list[Course] = []

    def create_course(self, course_id: str, title: str) -> Course:
        course = Course(course_id, title, self)
        self._courses.append(course)
        return course

    def display_teaching_courses(self) -> None:
        print(f"\nCourses taught by {self.name}:")
        if not self._courses:
            print("  No courses assigned.")
            return
        for course in self._courses:
            print(f"  - {course.course_id}: {course.title}")
