# app/api/organization.py
from fastapi import APIRouter, HTTPException

from app.crud.organization import (
    create_organization_career,
    create_organization_center,
    create_organization_contact,
    create_organization_partner,
    delete_organization_career,
    delete_organization_center,
    delete_organization_contact,
    delete_organization_partner,
    get_organization_career,
    get_organization_careers,
    get_organization_center,
    get_organization_centers,
    get_organization_contact,
    get_organization_contacts,
    get_organization_partner,
    get_organization_partners,
    update_organization_career,
    update_organization_center,
    update_organization_contact,
    update_organization_partner,
)
from app.dependencies.auth import AuthenticatedUser
from app.dependencies.database import Database
from app.schema.organization import (
    OrganizationCareerCreate,
    OrganizationCareerResponse,
    OrganizationCenterCreate,
    OrganizationCenterResponse,
    OrganizationContactCreate,
    OrganizationContactResponse,
    OrganizationPartnerCreate,
    OrganizationPartnerResponse,
)

router = APIRouter(prefix="/organization", tags=["organization"])


# OrganizationCenter Routes
@router.post("/centers/", response_model=OrganizationCenterResponse)
def create_center(
    center: OrganizationCenterCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_organization_center(db, center)


@router.get("/centers/", response_model=list[OrganizationCenterResponse])
def get_centers(db: Database):
    return get_organization_centers(db)


@router.get("/centers/{center_id}", response_model=OrganizationCenterResponse)
def get_center(center_id: int, db: Database):
    db_center = get_organization_center(db, center_id)
    if not db_center:
        raise HTTPException(status_code=404, detail="Center not found")
    return db_center


@router.put("/centers/{center_id}", response_model=OrganizationCenterResponse)
def update_center(
    center_id: int,
    center: OrganizationCenterCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_center = get_organization_center(db, center_id)
    if not db_center:
        raise HTTPException(status_code=404, detail="Center not found")
    return update_organization_center(db, center_id, center)


@router.delete("/centers/{center_id}")
def delete_center(center_id: int, db: Database, current_user: AuthenticatedUser):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_center = get_organization_center(db, center_id)
    if not db_center:
        raise HTTPException(status_code=404, detail="Center not found")
    delete_organization_center(db, center_id)
    return {"message": "Center deleted successfully"}


# OrganizationPartner Routes
@router.post("/partners/", response_model=OrganizationPartnerResponse)
def create_partner(
    partner: OrganizationPartnerCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_organization_partner(db, partner)


@router.get("/partners/", response_model=list[OrganizationPartnerResponse])
def get_partners(db: Database):
    return get_organization_partners(db)


@router.get("/partners/{partner_id}", response_model=OrganizationPartnerResponse)
def get_partner(partner_id: int, db: Database):
    db_partner = get_organization_partner(db, partner_id)
    if not db_partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    return db_partner


@router.put("/partners/{partner_id}", response_model=OrganizationPartnerResponse)
def update_partner(
    partner_id: int,
    partner: OrganizationPartnerCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_partner = get_organization_partner(db, partner_id)
    if not db_partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    return update_organization_partner(db, partner_id, partner)


@router.delete("/partners/{partner_id}")
def delete_partner(partner_id: int, db: Database, current_user: AuthenticatedUser):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_partner = get_organization_partner(db, partner_id)
    if not db_partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    delete_organization_partner(db, partner_id)
    return {"message": "Partner deleted successfully"}


# OrganizationCareer Routes
@router.post("/careers/", response_model=OrganizationCareerResponse)
def create_career(
    career: OrganizationCareerCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_organization_career(db, career)


@router.get("/careers/", response_model=list[OrganizationCareerResponse])
def get_careers(db: Database):
    return get_organization_careers(db)


@router.get("/careers/{career_id}", response_model=OrganizationCareerResponse)
def get_career(career_id: int, db: Database):
    db_career = get_organization_career(db, career_id)
    if not db_career:
        raise HTTPException(status_code=404, detail="Career not found")
    return db_career


@router.put("/careers/{career_id}", response_model=OrganizationCareerResponse)
def update_career(
    career_id: int,
    career: OrganizationCareerCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_career = get_organization_career(db, career_id)
    if not db_career:
        raise HTTPException(status_code=404, detail="Career not found")
    return update_organization_career(db, career_id, career)


@router.delete("/careers/{career_id}")
def delete_career(career_id: int, db: Database, current_user: AuthenticatedUser):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_career = get_organization_career(db, career_id)
    if not db_career:
        raise HTTPException(status_code=404, detail="Career not found")
    delete_organization_career(db, career_id)
    return {"message": "Career deleted successfully"}


# OrganizationContact Routes
@router.post("/contacts/", response_model=OrganizationContactResponse)
def create_contact(
    contact: OrganizationContactCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_organization_contact(db, contact)


@router.get("/contacts/", response_model=list[OrganizationContactResponse])
def get_contacts(db: Database):
    return get_organization_contacts(db)


@router.get("/contacts/{contact_id}", response_model=OrganizationContactResponse)
def get_contact(contact_id: int, db: Database):
    db_contact = get_organization_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.put("/contacts/{contact_id}", response_model=OrganizationContactResponse)
def update_contact(
    contact_id: int,
    contact: OrganizationContactCreate,
    db: Database,
    current_user: AuthenticatedUser,
):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_contact = get_organization_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return update_organization_contact(db, contact_id, contact)


@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Database, current_user: AuthenticatedUser):
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    db_contact = get_organization_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    delete_organization_contact(db, contact_id)
    return {"message": "Contact deleted successfully"}
