from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class IncomingMessage(BaseModel):
    # Модифицируйте атрибуты, чтобы они соответствовали заданию.
    title: Optional[str] = 'У этого сообщения нет заголовка'
    body: str = Field(None)
    contacts: Optional[str]
    secret_hash: str


class OutgoingMessage(BaseModel):
    # Опишите класс исходящего сообщения.

    class Config:
        orm_mode = True
        exclude = ['secret_hash']


# Модифицируйте эндпоинт так,
# чтобы он выполнял поставленную задачу.
@app.post(
        '/post-office',
        response_model=OutgoingMessage,
        response_model_exclude=True,
        response_model_exclude_defaults=True,)
def sloth(message: IncomingMessage):
    # Отсюда можно передать данные для обработки и сохранения в БД,
    # но этого писать мы не будем. И вам не нужно.
    return message
