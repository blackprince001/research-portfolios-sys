from fastapi import APIRouter, HTTPException, Form, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.crud.users import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
    get_user_by_username,
)
from app.dependencies.database import Database
from app.dependencies.jwt import create_token
from app.dependencies.auth import AuthenticatedUser
from app.schema.users import UserCreate, UserResponse, UserUpdate


from app.security import get_hash, password_matches_hashed

from datetime import timedelta
from typing import Annotated


router = APIRouter(tags=["users"])


@router.post("/auth/register", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Database):
    hashed_password = get_hash(user.password)
    try:
        db_user = create_user(db, username=user.username, password=hashed_password)
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# @router.get("/users/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, db: Database):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.get("/users/", response_model=list[UserResponse])
# def read_users(
#     db: Database,
#     skip: int = 0,
#     limit: int = 100,
# ):
#     users = get_users(db, skip=skip, limit=limit)
#     return users


# @router.put("/users/{user_id}", response_model=UserResponse)
# def update_user_route(user_id: int, user: UserUpdate, db: Database):
#     try:
#         db_user = update_user(db, user_id=user_id, username=user.username)
#         if db_user is None:
#             raise HTTPException(status_code=404, detail="User not found")
#         return db_user
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user_route(user_id: int, db: Database, current_user: AuthenticatedUser):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/auth/login")
async def login(db: Database, form_data: UserCreate):
    user = get_user_by_username(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    if not password_matches_hashed(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    access_token = create_token(
        data={"sub": str(user.id)}, expires_delta=timedelta(days=7)
    )

    return {"token": access_token, "user": UserResponse.from_orm(user)}


# @router.post("/auth/register")
# async def register(
#     db: Database,
#     username: str = Form(...),
#     password: str = Form(...),
# ):
#     hashed_password = get_hash(password)
#     try:
#         user = create_user(db, username=username, password=hashed_password)
#         access_token = create_token(
#             data={"sub": str(user.id)}, expires_delta=timedelta(days=7)
#         )
#         return {"token": access_token, "user": UserResponse.from_orm(user)}
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
