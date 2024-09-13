from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    profile = relationship("Profile", uselist=False, back_populates="user")
