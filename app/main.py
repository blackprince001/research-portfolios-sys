from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import organization, profiles, publications, teaching, users

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
app.include_router(teaching.router)
app.include_router(publications.router)
app.include_router(organization.router)


@app.get("/ping")
def ping_pong() -> dict[str, str]:
    return {"message": "pong"}
