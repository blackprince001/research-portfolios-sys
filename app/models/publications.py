from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class Publication(Base):
    __tablename__ = "publications"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    abstract: Mapped[str] = mapped_column(String, nullable=False)
    authors: Mapped[str] = mapped_column(String, nullable=False)
    publication_type: Mapped[str] = mapped_column(String, nullable=False)
    journal: Mapped[str | None] = mapped_column(String, nullable=True)
    conference: Mapped[str | None] = mapped_column(String, nullable=True)
    is_org: Mapped[bool] = mapped_column(Boolean, nullable=False)
    poster: Mapped[str | None] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    doi: Mapped[str | None] = mapped_column(String, nullable=True)
    url: Mapped[str | None] = mapped_column(String, nullable=True)
    pdf_link: Mapped[str | None] = mapped_column(String, nullable=True)

    user = relationship("User", back_populates="publications")
