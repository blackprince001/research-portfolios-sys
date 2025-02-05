from typing import Annotated

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.dependencies.database import Database
from app.models.users import User

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_authenticated_user(db: Database, token: str = Depends(reusable_oauth2)) -> User:
    token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credentials",
    )
    try:
        data: dict[str, str] = jwt.decode(
            token=token, key="something", algorithms=["HS256"]
        )
    except JWTError:
        raise token_exception

    user_id = int(data["sub"])

    user: User | None = db.get(User, user_id)

    if user is None:
        raise token_exception

    return user


AuthenticatedUser = Annotated[User, Depends(get_authenticated_user)]
