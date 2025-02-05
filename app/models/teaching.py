from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class Teaching(Base):
    __tablename__ = "teaching_experiences"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    institution: Mapped[str] = mapped_column(String, nullable=False)
    position: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    start_date: Mapped[str] = mapped_column(String, nullable=False)
    end_date: Mapped[str | None] = mapped_column(String, nullable=True)

    courses = relationship("Course", back_populates="teaching")
    user = relationship("User", back_populates="teaching_experiences")


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    teaching_id: Mapped[int] = mapped_column(
        ForeignKey("teaching_experiences.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

    teaching = relationship("Teaching", back_populates="courses")
