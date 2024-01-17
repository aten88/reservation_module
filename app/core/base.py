# noqa Файл-буфер для передачи моделей в модуль Alembic чтобы настроить env.py один раз

"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base # noqa
from app.models.meeting_room import MeetingRoom # noqa
