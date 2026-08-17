"""Demonstrate the object-oriented e-learning platform."""

from instructor import Instructor
from student import Student
from user import User


def main() -> None:
    # Student and Instructor inherit name, email, user_id, and display_profile
    # from the parent User class.
    instructor_one = Instructor(101, "Dr. Ananya Rao", "ananya@example.com")
    instructor_two = Instructor(102, "Prof. Rahul Mehta", "rahul@example.com")

    student_one = Student(201, "Aarav Sharma", "aarav@example.com")
    student_two = Student(202, "Meera Patel", "meera@example.com")

    python_course = instructor_one.create_course("CS101", "Python Programming")
    oop_course = instructor_one.create_course("CS102", "Object-Oriented Design")
    web_course = instructor_two.create_course("WEB101", "Web Development")

    print("=" * 64)
    print("E-LEARNING PLATFORM".center(64))
    print("=" * 64)

    print("\nUser profiles inherited from User:")
    for platform_user in (
        instructor_one,
        instructor_two,
        student_one,
        student_two,
    ):
        platform_user.display_profile()

    print("\nInheritance check:")
    print(f"  Student is a User: {isinstance(student_one, User)}")
    print(f"  Instructor is a User: {isinstance(instructor_one, User)}")

    instructor_one.display_teaching_courses()
    instructor_two.display_teaching_courses()

    print("\nEnrollments:")
    student_one.enroll(python_course)
    student_one.enroll(oop_course)
    student_two.enroll(python_course)
    student_two.enroll(web_course)

    student_one.update_progress(python_course, 75)
    student_one.update_progress(oop_course, 40)
    student_two.update_progress(python_course, 60)
    student_two.update_progress(web_course, 85)

    student_one.view_enrolled_courses()
    student_one.check_course_progress()
    student_two.view_enrolled_courses()
    student_two.check_course_progress()


if __name__ == "__main__":
    main()
