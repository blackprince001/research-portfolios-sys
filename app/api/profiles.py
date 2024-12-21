from fastapi import APIRouter, HTTPException

from app.crud.profiles import (
    create_profile,
    delete_profile,
    get_profile_by_user_id,
    update_profile,
)
from app.dependencies.auth import AuthenticatedUser
from app.dependencies.database import Database
from app.schema.profiles import ProfileCreate, ProfileRead

router = APIRouter(tags=["profiles"])


@router.post("/profiles/", response_model=ProfileRead)
def create_new_profile(
    current_user: AuthenticatedUser, profile: ProfileCreate, db: Database
):
    db_profile = create_profile(db, profile)
    if not db_profile:
        raise HTTPException(status_code=400, detail="Profile creation failed")
    return db_profile


@router.get("/profiles/{user_id}", response_model=ProfileRead)
def read_profile(user_id: int, db: Database):
    db_profile = get_profile_by_user_id(db, user_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.put("/profiles/{profile_id}", response_model=ProfileRead)
def update_existing_profile(
    current_user: AuthenticatedUser,
    profile_id: int,
    profile: ProfileCreate,
    db: Database,
):
    db_profile = update_profile(db, profile_id, profile)
    if not db_profile:
        raise HTTPException(
            status_code=404, detail="Profile not found or update failed"
        )
    return db_profile


@router.delete("/profiles/{profile_id}")
def delete_existing_profile(
    current_user: AuthenticatedUser, profile_id: int, db: Database
):
    db_profile = delete_profile(db, profile_id)
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted successfully"}
