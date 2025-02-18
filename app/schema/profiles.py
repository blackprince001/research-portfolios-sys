from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class ProfileCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    name: str
    org_role: str
    home_content: Optional[List[str]] = None
    profile_image: Optional[str] = None
    projects: Optional[List[Dict[str, str]]] = None
    teachings: Optional[List[str]] = None
    cv_link: Optional[str] = None


class ProfileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    org_role: str
    home_content: Optional[List[str]] = None
    projects: Optional[List[Dict[str, str]]] = None
    teachings: Optional[List[str]] = None
    cv_link: Optional[str] = None
