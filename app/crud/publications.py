# app/crud/publications.py
from sqlalchemy.orm import Session
from app.models.publications import Publication
from app.schema.publications import PublicationCreate


def create_publication(db: Session, publication: PublicationCreate) -> Publication:
    db_publication = Publication(**publication.dict())
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def get_user_publications(db: Session, user_id: int) -> list[Publication]:
    return db.query(Publication).filter(Publication.user_id == user_id).all()


def get_publications(db: Session) -> Publication | None:
    return db.query(Publication).all()


def get_publication(db: Session, pub_id: int) -> Publication | None:
    return db.query(Publication).filter(Publication.id == pub_id).first()


def update_publication(
    db: Session, pub_id: int, publication: PublicationCreate
) -> Publication | None:
    db_pub = get_publication(db, pub_id)
    if db_pub:
        for key, value in publication.dict(exclude_unset=True).items():
            setattr(db_pub, key, value)
        db.commit()
        db.refresh(db_pub)
    return db_pub


def delete_publication(db: Session, pub_id: int) -> bool:
    db_pub = get_publication(db, pub_id)
    if db_pub:
        db.delete(db_pub)
        db.commit()
        return True
    return False
