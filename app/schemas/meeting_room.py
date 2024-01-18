from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)

    @validator('name')
    def name_is_not_empty(cls, value):
        if not value.strip():
            raise ValueError('Поле name не может быть пустым.')
        return value

    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomDB(MeetingRoomBase):
    id: int

    class Config:
        orm_mode = True
