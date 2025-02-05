from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    publications = relationship(
        "Publication", back_populates="user", cascade="all, delete-orphan"
    )
    teaching_experiences = relationship(
        "Teaching", back_populates="user", cascade="all, delete-orphan"
    )
    profile = relationship(
        "Profile", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
