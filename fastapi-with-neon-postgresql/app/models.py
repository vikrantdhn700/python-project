from sqlalchemy import Column, ForeignKey, Integer, String, Text, Numeric, DateTime, text
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(320), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    credit_hours = Column(Integer, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    status = Column(String(20), nullable=False)
    enrolled_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False
    )
