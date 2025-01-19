from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = getenv("DATABASE_URL", "sqlite:///documents.blogger.sqlite")

engine = create_engine(
    database_url,
    echo=True,
    connect_args={"check_same_thread": False},
)

SessionMaker = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
