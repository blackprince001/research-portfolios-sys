# app/api/teaching.py
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.database import Database
from app.dependencies.auth import AuthenticatedUser
from app.crud import teaching as crud
from app.schema.teaching import (
    TeachingCreate,
    TeachingResponse,
    CourseCreate,
    CourseResponse,
)

router = APIRouter(prefix="/teaching", tags=["teaching"])


@router.post("/", response_model=TeachingResponse)
def create_teaching_experience(
    teaching: TeachingCreate, db: Database, current_user: AuthenticatedUser
):
    if teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_teaching(db, teaching)


@router.get("/user/{user_id}", response_model=list[TeachingResponse])
def get_user_teaching_experiences(user_id: int, db: Database):
    return crud.get_user_teaching_experiences(db, user_id)


@router.get("/{teaching_id}", response_model=TeachingResponse)
def get_teaching_experience(teaching_id: int, db: Database):
    db_teaching = crud.get_teaching(db, teaching_id)
    if not db_teaching or db_teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return db_teaching


@router.put("/{teaching_id}", response_model=TeachingResponse)
def update_teaching_experience(
    teaching_id: int,
    teaching: TeachingCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    db_teaching = crud.get_teaching(db, teaching_id)
    if not db_teaching or db_teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.update_teaching(db, teaching_id, teaching)


@router.delete("/{teaching_id}")
def delete_teaching_experience(
    teaching_id: int, db: Database, current_user: AuthenticatedUser
):
    db_teaching = crud.get_teaching(db, teaching_id)
    if not db_teaching or db_teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    crud.delete_teaching(db, teaching_id)
    return {"message": "Teaching experience deleted successfully"}


# Course-specific endpoints
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Database, current_user: AuthenticatedUser):
    # Verify the teaching experience belongs to the current user
    teaching = crud.get_teaching(db, course.teaching_id)
    if not teaching or teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_course(db, course)


@router.get("/courses/{teaching_id}", response_model=list[CourseResponse])
def get_teaching_courses(teaching_id: int, db: Database):
    teaching = crud.get_teaching(db, teaching_id)
    if not teaching or teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_teaching_courses(db, teaching_id)


@router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int, course: CourseCreate, db: Database, current_user: AuthenticatedUser
):
    db_course = crud.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    teaching = crud.get_teaching(db, db_course.teaching_id)
    if not teaching or teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return crud.update_course(db, course_id, course)


@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Database, current_user: AuthenticatedUser):
    db_course = crud.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    teaching = crud.get_teaching(db, db_course.teaching_id)
    if not teaching or teaching.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    crud.delete_course(db, course_id)
    return {"message": "Course deleted successfully"}
