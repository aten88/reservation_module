# app/api/meeting_room.py

from fastapi import APIRouter

from app.crud.meeting_room import create_meeting_room
from app.schemas.meeting_room import MeetingRoomCreate

router = APIRouter()


@router.post('/meeting_rooms/')
async def create_new_meeting_room(
        meeting_room: MeetingRoomCreate,
):
    new_room = await create_meeting_room(meeting_room)
    return new_room
