from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.schemas import (
    StudentListRead, StudentCreate, StudentUpdate,
    CourseListRead, CourseCreate, CourseUpdate,
    EnrollmentListRead, EnrollmentCreate, EnrollmentUpdate
)
from app.models import (
    Student, Course, Enrollment
)

app = FastAPI(title="FastAPI with Neon PostgreSQL")


def find_single_data(data_model, single_id: int):
    db = SessionLocal()
    try:
        return db.query(data_model).filter(data_model.id == single_id).first()
    finally:
        db.close()

# Get Students


@app.get("/students/", response_model=StudentListRead, tags=["students"])
def get_students(db: Session = Depends(get_db)):
    return {
        "status": "success",
        "message": "Successfully fetched",
        "data": db.query(Student).all()
    }


# Get Student
@app.get("/students/{student_id}", response_model=StudentListRead, tags=["students"])
def get_student(student_id: int):
    student = find_single_data(Student, student_id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return {
        "status": "success",
        "message": "Successfully fetched",
        "data": [student]
    }


# Create a new student


@app.post("/students/", response_model=StudentListRead, tags=["students"])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(first_name=student.first_name.strip(),
                          last_name=student.last_name.strip(), email=student.email.strip())
    db.add(new_student)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Student email already exists. Please use a different email."
        )
    db.refresh(new_student)
    return {
        "status": "success",
        "message": "Successfully created",
        "data": [new_student]
    }

# Update student by id


@app.put("/students/{student_id}", response_model=StudentListRead, tags=["students"])
@app.patch("/students/{student_id}", response_model=StudentListRead, tags=["students"])
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    existing_student = find_single_data(Student, student_id)
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_student = db.merge(existing_student)
    if student.first_name is not None:
        existing_student.first_name = student.first_name.strip()
    if student.last_name is not None:
        existing_student.last_name = student.last_name.strip()
    if student.email is not None:
        existing_student.email = student.email.strip()
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Student email already exists. Please use a different email."
        )
    db.refresh(existing_student)
    return {
        "status": "success",
        "message": "Successfully updated",
        "data": [existing_student]
    }

# Delete Student by id


@app.delete("/students/{student_id}", response_model=StudentListRead, tags=["students"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    existing_student = find_single_data(Student, id)
    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db.delete(existing_student)
    db.commit()
    return {
        "status": "success",
        "message": "Student deleted",
        "data": [existing_student]
    }


# Get courses


@app.get("/courses/", response_model=CourseListRead, tags=["courses"])
def get_courses(db: Session = Depends(get_db)):
    return {
        "status": "success",
        "message": "Successfully fetched",
        "data": db.query(Course).all()
    }

# Get Course by id


@app.get("/courses/{course_id}", response_model=CourseListRead, tags=["courses"])
def get_courses(course_id: int, db: Session = Depends(get_db)):
    course = find_single_data(Course, course_id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    return {
        "status": "success",
        "message": "Successfully fetched",
        "data": [course]
    }

# Create a new course


@app.post("/courses/", response_model=CourseListRead, tags=["courses"])
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(
        code=course.code,
        title=course.title.strip(),
        description=course.description.strip(),
        credit_hours=course.credit_hours,
        price=course.price
    )
    db.add(new_course)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Course code already exists. Please use a different code."
        )
    db.refresh(new_course)
    return {
        "status": "success",
        "message": "Successfully created",
        "data": [new_course]
    }


# Update course by id
@app.put("/courses/{course_id}", response_model=CourseListRead, tags=["courses"])
@app.patch("/courses/{course_id}", response_model=CourseListRead, tags=["courses"])
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    existing_course = find_single_data(Course, course_id)
    if existing_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    existing_course = db.merge(existing_course)
    if course.code is not None:
        existing_course.code = course.code
    if course.title is not None:
        existing_course.title = course.title.strip()
    if course.description is not None:
        existing_course.description = course.description.strip()
    if course.credit_hours is not None:
        existing_course.credit_hours = course.credit_hours
    if course.price is not None:
        existing_course.price = course.price

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Course code already exists. Please use a different code."
        )

    db.refresh(existing_course)
    return {
        "status": "success",
        "message": "Successfully updated",
        "data": [existing_course]
    }


# Delete course by id
@app.delete("/courses/{course_id}", response_model=CourseListRead, tags=["courses"])
def delete_course(course_id: int, db: Session = Depends(get_db)):
    existing_course = find_single_data(Course, course_id)
    if existing_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    existing_course = db.merge(existing_course)
    db.delete(existing_course)
    db.commit()
    return {
        "status": "success",
        "message": "Course deleted",
        "data": [existing_course]
    }

# Create Enrollment


@app.post("/enrollments/", response_model=EnrollmentListRead, tags=["enrollments"])
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    student = find_single_data(Student, enrollment.student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    course = find_single_data(Course, enrollment.course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    already_enrolled = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment.student_id,
        Enrollment.course_id == enrollment.course_id
    ).first()
    if already_enrolled is not None:
        raise HTTPException(
            status_code=409,
            detail="Student is already enrolled in this course."
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        status="active"
    )

    db.add(new_enrollment)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Enrollment could not be created."
        )
    db.refresh(new_enrollment)
    return {
        "status": "success",
        "message": "Successfully enrolled",
        "data": [{
            "id": new_enrollment.id,
            "student_name": f"{student.first_name} {student.last_name}",
            "course_title": course.title,
            "enrolled_at": new_enrollment.enrolled_at,
            "status": new_enrollment.status
        }]
    }

# Get Enrollments


@app.get("/enrollments/", response_model=EnrollmentListRead, tags=["enrollments"])
def get_enrollments(db: Session = Depends(get_db)):
    enrollment_data = db.query(Enrollment, Student, Course).join(
        Student, Enrollment.student_id == Student.id
    ).join(
        Course, Enrollment.course_id == Course.id
    ).all()

    return {
        "status": "success",
        "message": "Successfully fetched",
        "data": [
            {
                "id": enrollment.id,
                "student_name": f"{student.first_name} {student.last_name}",
                "course_title": course.title,
                "enrolled_at": enrollment.enrolled_at,
                "status": enrollment.status
            }
            for enrollment, student, course in enrollment_data
        ]
    }


# Delete Enrollments
@app.delete("/enrollments/{enrollment_id}", response_model=EnrollmentListRead, tags=["enrollments"])
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    existing_enrollment = find_single_data(Enrollment, enrollment_id)
    if existing_enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )
    db.delete(existing_enrollment)
    return {
        "status": "success",
        "message": "Successfully deleted",
        "data": existing_enrollment
    }
