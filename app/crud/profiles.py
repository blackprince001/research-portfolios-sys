from sqlalchemy.orm import Session

from app.models.profiles import Profile
from app.schema.profiles import ProfileCreate


def get_profile_by_user_id(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def update_profile(db: Session, profile_id: int, updated_data: ProfileCreate):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not db_profile:
        return None
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()
    return db_profile
