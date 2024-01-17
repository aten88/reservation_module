from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., max_length=100)

    @validator('name')
    def name_is_not_empty(cls, value):
        if not value.strip():
            raise ValueError('Поле name не может быть пустым.')
        return value
    description: Optional[str]
