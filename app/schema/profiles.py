from typing import Dict, List, Optional

from pydantic import BaseModel


class ProfileCreate(BaseModel):
    user_id: int
    home_content: Optional[List[str]] = (
        None  # List of paragraphs for the home/about section
    )
    projects: Optional[List[Dict[str, str]]] = (
        None  # List of projects (could be more complex with dict)
    )
    teachings: Optional[List[str]] = None  # List of teaching experiences
    cv_link: Optional[str] = None

    class Config:
        orm_mode = True


class ProfileRead(BaseModel):
    id: int
    user_id: int
    home_content: Optional[List[str]] = None
    projects: Optional[List[Dict[str, str]]] = None
    teachings: Optional[List[str]] = None
    cv_link: Optional[str] = None

    class Config:
        orm_mode = True
