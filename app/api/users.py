from fastapi import APIRouter, HTTPException

from app.crud.users import create_user, delete_user, get_user, get_users, update_user
from app.dependencies.database import Database
from app.schema.users import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("/users/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Database):
    try:
        db_user = create_user(db, username=user.username, password=user.password)
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Database):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/", response_model=list[UserResponse])
def read_users(
    db: Database,
    skip: int = 0,
    limit: int = 100,
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_route(user_id: int, user: UserUpdate, db: Database):
    try:
        db_user = update_user(db, user_id=user_id, username=user.username)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user_route(user_id: int, db: Database):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
