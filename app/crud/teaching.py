# app/crud/teaching.py
from sqlalchemy.orm import Session
from app.models.teaching import Teaching, Course
from app.schema.teaching import TeachingCreate, CourseCreate


def create_teaching(db: Session, teaching: TeachingCreate) -> Teaching:
    db_teaching = Teaching(**teaching.dict(exclude={"courses"}))
    db.add(db_teaching)
    db.commit()
    db.refresh(db_teaching)

    # Add associated courses if provided
    if teaching.courses:
        for course in teaching.courses:
            db_course = Course(teaching_id=db_teaching.id, **course.dict())
            db.add(db_course)
        db.commit()
        db.refresh(db_teaching)

    return db_teaching


def get_user_teaching_experiences(db: Session, user_id: int) -> list[Teaching]:
    return db.query(Teaching).filter(Teaching.user_id == user_id).all()


def get_teaching(db: Session, teaching_id: int) -> Teaching | None:
    return db.query(Teaching).filter(Teaching.id == teaching_id).first()


def update_teaching(
    db: Session, teaching_id: int, teaching: TeachingCreate
) -> Teaching | None:
    db_teaching = get_teaching(db, teaching_id)
    if db_teaching:
        # Update teaching experience fields
        for key, value in teaching.dict(
            exclude={"courses"}, exclude_unset=True
        ).items():
            setattr(db_teaching, key, value)

        # Handle courses update
        if teaching.courses:
            # Remove existing courses
            db.query(Course).filter(Course.teaching_id == teaching_id).delete()

            # Add new courses
            for course in teaching.courses:
                db_course = Course(teaching_id=teaching_id, **course.dict())
                db.add(db_course)

        db.commit()
        db.refresh(db_teaching)
    return db_teaching


def delete_teaching(db: Session, teaching_id: int) -> bool:
    db_teaching = get_teaching(db, teaching_id)
    if db_teaching:
        # This will cascade delete associated courses
        db.delete(db_teaching)
        db.commit()
        return True
    return False


# Course-specific CRUD operations
def create_course(db: Session, course: CourseCreate) -> Course:
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_course(db: Session, course_id: int) -> Course | None:
    return db.query(Course).filter(Course.id == course_id).first()


def get_teaching_courses(db: Session, teaching_id: int) -> list[Course]:
    return db.query(Course).filter(Course.teaching_id == teaching_id).all()


def update_course(db: Session, course_id: int, course: CourseCreate) -> Course | None:
    db_course = get_course(db, course_id)
    if db_course:
        for key, value in course.dict(exclude_unset=True).items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int) -> bool:
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
        return True
    return False
