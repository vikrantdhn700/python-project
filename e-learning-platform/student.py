"""Student model inherited from User."""

from course import Course
from user import User


class Student(User):
    """A user who can enroll in courses and track progress."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id, name, email)
        self._enrollments: dict[Course, int] = {}

    def enroll(self, course: Course) -> None:
        if course in self._enrollments:
            print(f"{self.name} is already enrolled in {course.title}.")
            return
        self._enrollments[course] = 0
        print(f"{self.name} enrolled in {course.title}.")

    def update_progress(self, course: Course, progress: int) -> None:
        if course not in self._enrollments:
            raise ValueError(f"{self.name} is not enrolled in {course.title}.")
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100.")
        self._enrollments[course] = progress

    def view_enrolled_courses(self) -> None:
        print(f"\nCourses enrolled by {self.name}:")
        if not self._enrollments:
            print("  No enrolled courses.")
            return
        for course in self._enrollments:
            print(f"  - {course}")

    def check_course_progress(self) -> None:
        print(f"\nCourse progress for {self.name}:")
        if not self._enrollments:
            print("  No enrolled courses.")
            return
        for course, progress in self._enrollments.items():
            print(f"  - {course.title}: {progress}%")
