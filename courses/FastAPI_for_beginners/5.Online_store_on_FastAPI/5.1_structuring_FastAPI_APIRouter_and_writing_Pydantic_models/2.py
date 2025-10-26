"""
Разработайте веб-приложение на фреймворке FastAPI, которое подключает маршруты
для работы с заметками, определённые в отдельном модуле с использованием
APIRouter.

Вам необходимо:
Создать основное приложение FastAPI.
Подключить маршруты для заметок, определённые в модуле app.routers.notes, где
находится APIRouter.

Код в app.routers.notes (чтобы было ясно, что подключается):
from fastapi import APIRouter

notes_router = APIRouter(prefix="/notes", tags=["notes"])


@notes_router.get("/")
def root():
    return "Notes API is working"
"""

from fastapi import FastAPI

from app.routers.notes import notes_router

app = FastAPI()
app.include_router(notes_router)
