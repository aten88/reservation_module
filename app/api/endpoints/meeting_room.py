from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.meeting_room import meeting_room_crud
from app.schemas.meeting_room import (
    MeetingRoomCreate, MeetingRoomDB,
    MeetingRoomUpdate
)
from app.api.validators import check_meeting_room_exist, check_name_duplicate

router = APIRouter()


@router.post(
        '/',
        response_model=MeetingRoomDB,
        response_model_exclude_none=True,
    )
async def create_new_meeting_room(
        meeting_room: MeetingRoomCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(meeting_room.name, session)
    new_room = await meeting_room_crud.create(meeting_room, session)
    return new_room


@router.get(
        '/',
        response_model=List[MeetingRoomDB],
        response_model_exclude_none=True
    )
async def get_all_meeting_rooms(
    session: AsyncSession = Depends(get_async_session)
):
    all_rooms = await meeting_room_crud.get_multi(session)
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
    meeting_room = await check_meeting_room_exist(meeting_room_id, session)

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    meeting_room = await meeting_room_crud.update(
        meeting_room, obj_in, session
    )
    return meeting_room


@router.delete(
        '/{meeting_room_id}',
        response_model=MeetingRoomDB,
        response_model_exclude_none=True,
)
async def remove_meeting_room(
    meeting_room_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    meeting_room = await check_meeting_room_exist(meeting_room_id, session)
    meeting_room = await meeting_room_crud.remove(meeting_room, session)
    return meeting_room
