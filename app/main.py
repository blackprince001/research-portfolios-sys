from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import profiles, users
from app.database.core import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(profiles.router)


@app.get("/ping")
def ping_pong() -> dict[str, str]:
    return {"message": "pong"}
