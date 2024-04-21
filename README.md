# Модуль бронирования переговорных комнат
## Описание проекта:
Данный проект-это модуль бронирования комнат для переговоров на определенные временные промежутки. Модуль может создавать, редактировать, удалять и завершать бронирование. Модуль реализован при помощи фреймворка FastApi
## Возможности проекта:
- Создание переговорных комнат.
- Создание бронирований.
- Учет ранее созданных интервалов времени при бронировании во избежание пересечений.
- Механизм авторизации и аутентификации.
- API интерфейс и автодокументирование проекта.
- Использование класса CRUDBase с целью оптимизации структуры проекта.
- Асинхронный подход в реализации проекта.
#### Стек проекта: Python 3, FastAPI, Alembic, SQLAlchemy.

## Установка и запуск проекта:
 - Клонировать репозиторий локально:
 ```
   git clone git@github.com:aten88/reservation_module.git
 ```
 - В корневом каталоге создайте файл .env и добавьте в него данные (при необходимости):
 ```
APP_TITLE=some_title_example
DESCRIPTION=Some_descrition_example
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=Some_password
FIRST_SUPERUSER_EMAIL=e-mail@example.com
FIRST_SUPERUSER_PASSWORD=some_Password     # Пароль для суперюзера по умолчанию(при желании)
 ```
 - Установите и активируйте виртуальное окружение:
 ```
  python -m venv venv
 ```
   - Windows:
      ```
       source/venv/scripts/activate
      ```  
   - Linux/Mac OS:
      ```
       source/venv/bin/activate
      ```
 - Установите зависимости:
  ```
   pip install -r requirements.txt
  ```
 - Создайте миграции:
  ```
   alembic revision --autogenerate -m "First migration"
  ``` 
 - Примените миграции:
  ```
   alembic upgrade head
  ```
 - Запустите проект:
  ```
   uvicorn app.main:app  --reload
  ```
## Документация проекта:
 - При запущенном проекте откройте одну из ссылкок в браузере:

    Swagger:
     ```
      http://127.0.0.1:8000/docs
     ```
    Redoc:
     ```
      http://127.0.0.1:8000/redoc
     ```
### Автор: Алексей Тен.
