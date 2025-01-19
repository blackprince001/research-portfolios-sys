from pydantic import BaseModel, ConfigDict
from typing import Optional


class PublicationBase(BaseModel):
    title: str
    abstract: str
    authors: str
    publication_type: str
    journal: Optional[str] = None
    conference: Optional[str] = None
    year: int
    doi: Optional[str] = None
    url: Optional[str] = None
    pdf_link: Optional[str] = None


class PublicationCreate(PublicationBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: int


class PublicationResponse(PublicationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int


class PublicationsResponse(PublicationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int