# app/api/meeting_room.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.meeting_room import (
    create_meeting_room, get_room_id_by_name,
    read_all_rooms_from_db, get_meeting_room_by_id,
    update_meeting_room

)
from app.schemas.meeting_room import (
    MeetingRoomCreate, MeetingRoomDB,
    MeetingRoomUpdate
)

router = APIRouter(
    prefix='/meeting_rooms',
    tags=['Meeting Rooms']
    )


@router.post(
        '/',
        response_model=MeetingRoomDB,
        response_model_exclude_none=True,
    )
async def create_new_meeting_room(
        meeting_room: MeetingRoomCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(meeting_room, session)
    new_room = await create_meeting_room(meeting_room, session)
    return new_room


@router.get(
        '/',
        response_model=List[MeetingRoomDB],
        response_model_exclude_none=True
    )
async def get_all_meeting_rooms(
    session: AsyncSession = Depends(get_async_session)
):
    all_rooms = await read_all_rooms_from_db(session)
    if all_rooms is None:
        raise HTTPException(
            status_code=404,
            detail='В БД нет ни одной записи о переговорных комнатах.'
        )
    return all_rooms


@router.patch(
        '/{meeting_room_id}',
        response_model=MeetingRoomDB,
        response_model_exclude_none=True,
)
async def partially_update_meeting_room(
    meeting_room_id: int,
    obj_in: MeetingRoomUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    meeting_room = await get_meeting_room_by_id(
        meeting_room_id, session
    )

    if meeting_room is None:
        raise HTTPException(
            status_code=404,
            detail='Переговорка не найдена!'
        )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    meeting_room = await update_meeting_room(meeting_room, obj_in, session)
    return meeting_room


async def check_name_duplicate(
    room_name: str,
    session: AsyncSession,
) -> None:
    room_id = await get_room_id_by_name(room_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )
