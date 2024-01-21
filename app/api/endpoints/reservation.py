from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_reservation_intersections,
    check_meeting_room_exist,
    check_reservation_before_edit
)
from app.core.db import get_async_session
from app.crud.reservation import reservation_crud
from app.schemas.reservation import ReservationCreate, ReservationDB

router = APIRouter()


@router.post('/', response_model=ReservationDB)
async def create_reservation(
        reservation: ReservationCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_meeting_room_exist(
        reservation.meetingroom_id, session
    )
    await check_reservation_intersections(
        **reservation.dict(), session=session
    )
    new_reservation = await reservation_crud.create(
        reservation, session
    )
    return new_reservation


@router.get('/', response_model=List[ReservationDB])
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session)
):
    reservations = await reservation_crud.get_multi(session)
    return reservations


@router.delete(
    '/{reservation_id}',
    response_model=ReservationDB
)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    reservation = await check_reservation_before_edit(reservation_id, session)

    reservation = await reservation_crud.remove(reservation, session)

    return reservation
