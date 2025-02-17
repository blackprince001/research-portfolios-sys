from sqlalchemy import JSON, Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core import Base


class OrganizationCenter(Base):
    __tablename__ = "organization_centers"

    id: Mapped[int] = mapped_column(primary_key=True)
    center_name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)


class OrganizationPartner(Base):
    __tablename__ = "organization_partners"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    socials: Mapped[list] = mapped_column(JSON, nullable=False)
    logo_url: Mapped[str] = mapped_column(String, nullable=False)


class OrganizationCareer(Base):
    __tablename__ = "organization_careers"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    is_closed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class OrganizationContact(Base):
    __tablename__ = "organization_contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    is_closed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
