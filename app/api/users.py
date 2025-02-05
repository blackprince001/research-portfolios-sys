from datetime import timedelta

from fastapi import APIRouter, HTTPException, status

from app.crud.users import (
    create_user,
    delete_user,
    get_user_by_username,
)
from app.dependencies.auth import AuthenticatedUser
from app.dependencies.database import Database
from app.dependencies.jwt import create_token
from app.schema.users import UserCreate, UserResponse
from app.security import get_hash, password_matches_hashed

router = APIRouter(tags=["users"])


@router.post("/auth/register", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Database):
    hashed_password = get_hash(user.password)
    try:
        db_user = create_user(db, username=user.username, password=hashed_password)
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


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
