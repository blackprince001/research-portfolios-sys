from typing import List

from pydantic import BaseModel, ConfigDict


# OrganizationCenter Schemas
class OrganizationCenterBase(BaseModel):
    center_name: str
    location: str


class OrganizationCenterCreate(OrganizationCenterBase):
    model_config = ConfigDict(from_attributes=True)


class OrganizationCenterResponse(OrganizationCenterBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


# OrganizationPartner Schemas
class OrganizationPartnerBase(BaseModel):
    name: str
    socials: List[str]
    logo_url: str


class OrganizationPartnerCreate(OrganizationPartnerBase):
    model_config = ConfigDict(from_attributes=True)


class OrganizationPartnerResponse(OrganizationPartnerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


# OrganizationCareer Schemas
class OrganizationCareerBase(BaseModel):
    title: str
    description: str
    type: str
    is_closed: bool = False


class OrganizationCareerCreate(OrganizationCareerBase):
    model_config = ConfigDict(from_attributes=True)


class OrganizationCareerResponse(OrganizationCareerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
