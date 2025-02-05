from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = getenv(
    "DATABASE_URL",
    "postgresql://postgres:[Password]@db.jfvuecmugsuujuoqngkp.supabase.co:5432/postgres",
)

engine = create_engine(
    database_url,
    echo=True,
)


SessionMaker = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
