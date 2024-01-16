from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Простое описание сервиса брон. переговорок'
    databse_url: str

    class Config:
        env_file = '.env'


settings = Settings()
