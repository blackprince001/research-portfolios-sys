# app/api/publications.py
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.database import Database
from app.dependencies.auth import AuthenticatedUser
from app.crud import publications as crud
from app.schema.publications import PublicationCreate, PublicationResponse

router = APIRouter(prefix="/publications", tags=["publications"])


@router.post("/", response_model=PublicationResponse)
def create_publication(
    publication: PublicationCreate, db: Database, current_user: AuthenticatedUser
):
    if publication.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_publication(db, publication)


@router.get("/user/{user_id}", response_model=list[PublicationResponse])
def get_user_publications(user_id: int, db: Database, current_user: AuthenticatedUser):
    return crud.get_user_publications(db, user_id)


@router.put("/{pub_id}", response_model=PublicationResponse)
def update_publication(
    pub_id: int,
    publication: PublicationCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    db_pub = crud.get_publication(db, pub_id)
    if not db_pub or db_pub.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.update_publication(db, pub_id, publication)


@router.delete("/{pub_id}")
def delete_publication(pub_id: int, db: Database, current_user: AuthenticatedUser):
    db_pub = crud.get_publication(db, pub_id)
    if not db_pub or db_pub.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    crud.delete_publication(db, pub_id)
    return {"message": "Publication deleted successfully"}
