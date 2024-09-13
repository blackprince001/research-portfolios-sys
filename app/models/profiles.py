from sqlalchemy import JSON, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, unique=True
    )
    home_content: Mapped[list] = mapped_column(
        JSON, nullable=True
    )  # About/Bio information as a list of paragraphs or sections
    projects: Mapped[list] = mapped_column(
        JSON, nullable=True
    )  # List of projects (e.g., dictionaries with details)
    teachings: Mapped[list] = mapped_column(
        JSON, nullable=True
    )  # List of teaching experiences
    cv_link: Mapped[str] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="profile")
