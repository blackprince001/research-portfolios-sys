from sqlalchemy.orm import Session

from app.models.organization import (
    OrganizationCareer,
    OrganizationCenter,
    OrganizationPartner,
)
from app.schema.organization import (
    OrganizationCareerCreate,
    OrganizationCenterCreate,
    OrganizationPartnerCreate,
)


def create_organization_center(
    db: Session, center: OrganizationCenterCreate
) -> OrganizationCenter:
    db_center = OrganizationCenter(**center.dict())
    db.add(db_center)
    db.commit()
    db.refresh(db_center)
    return db_center


def get_organization_centers(db: Session) -> list[OrganizationCenter]:
    return db.query(OrganizationCenter).all()


def get_organization_center(db: Session, center_id: int) -> OrganizationCenter | None:
    return (
        db.query(OrganizationCenter).filter(OrganizationCenter.id == center_id).first()
    )


def update_organization_center(
    db: Session, center_id: int, center: OrganizationCenterCreate
) -> OrganizationCenter | None:
    db_center = get_organization_center(db, center_id)
    if db_center:
        for key, value in center.dict(exclude_unset=True).items():
            setattr(db_center, key, value)
        db.commit()
        db.refresh(db_center)
    return db_center


def delete_organization_center(db: Session, center_id: int) -> bool:
    db_center = get_organization_center(db, center_id)
    if db_center:
        db.delete(db_center)
        db.commit()
        return True
    return False


def create_organization_partner(
    db: Session, partner: OrganizationPartnerCreate
) -> OrganizationPartner:
    db_partner = OrganizationPartner(**partner.dict())
    db.add(db_partner)
    db.commit()
    db.refresh(db_partner)
    return db_partner


def get_organization_partners(db: Session) -> list[OrganizationPartner]:
    return db.query(OrganizationPartner).all()


def get_organization_partner(
    db: Session, partner_id: int
) -> OrganizationPartner | None:
    return (
        db.query(OrganizationPartner)
        .filter(OrganizationPartner.id == partner_id)
        .first()
    )


def update_organization_partner(
    db: Session, partner_id: int, partner: OrganizationPartnerCreate
) -> OrganizationPartner | None:
    db_partner = get_organization_partner(db, partner_id)
    if db_partner:
        for key, value in partner.dict(exclude_unset=True).items():
            setattr(db_partner, key, value)
        db.commit()
        db.refresh(db_partner)
    return db_partner


def delete_organization_partner(db: Session, partner_id: int) -> bool:
    db_partner = get_organization_partner(db, partner_id)
    if db_partner:
        db.delete(db_partner)
        db.commit()
        return True
    return False


def create_organization_career(
    db: Session, career: OrganizationCareerCreate
) -> OrganizationCareer:
    db_career = OrganizationCareer(**career.dict())
    db.add(db_career)
    db.commit()
    db.refresh(db_career)
    return db_career


def get_organization_careers(db: Session) -> list[OrganizationCareer]:
    return db.query(OrganizationCareer).all()


def get_organization_career(db: Session, career_id: int) -> OrganizationCareer | None:
    return (
        db.query(OrganizationCareer).filter(OrganizationCareer.id == career_id).first()
    )


def update_organization_career(
    db: Session, career_id: int, career: OrganizationCareerCreate
) -> OrganizationCareer | None:
    db_career = get_organization_career(db, career_id)
    if db_career:
        for key, value in career.dict(exclude_unset=True).items():
            setattr(db_career, key, value)
        db.commit()
        db.refresh(db_career)
    return db_career


def delete_organization_career(db: Session, career_id: int) -> bool:
    db_career = get_organization_career(db, career_id)
    if db_career:
        db.delete(db_career)
        db.commit()
        return True
    return False
