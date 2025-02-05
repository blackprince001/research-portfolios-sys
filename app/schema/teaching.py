from typing import Optional

from pydantic import BaseModel, ConfigDict


class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None


class CourseCreate(CourseBase):
    model_config = ConfigDict(from_attributes=True)
    teaching_id: int


class CourseResponse(CourseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    teaching_id: int


class TeachingBase(BaseModel):
    institution: str
    position: str
    description: str
    start_date: str
    end_date: Optional[str] = None


class TeachingCreate(TeachingBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    courses: list[CourseBase]


class TeachingResponse(TeachingBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    courses: list[CourseResponse]
