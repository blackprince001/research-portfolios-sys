from sqlalchemy import JSON, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    org_role: Mapped[str] = mapped_column(String, nullable=False)
    profile_image: Mapped[str] = mapped_column(String, nullable=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, unique=True
    )
    home_content: Mapped[list] = mapped_column(JSON, nullable=True)
    projects: Mapped[list] = mapped_column(JSON, nullable=True)
    teachings: Mapped[list] = mapped_column(JSON, nullable=True)
    cv_link: Mapped[str] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="profile")
