from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Простое описание сервиса брон. переговорок'

    class Config:
        env_file = '.env'


settings = Settings()
