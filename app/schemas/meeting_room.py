from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_is_not_none(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomBase):
    id: int

    class Config:
        orm_mode = True
