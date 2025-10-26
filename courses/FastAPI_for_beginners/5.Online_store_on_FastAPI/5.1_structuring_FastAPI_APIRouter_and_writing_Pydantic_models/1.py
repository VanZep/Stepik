"""
Cоздайте APIRouter для работы с заметками, в котором эндпоинт должен
возвращать приветственное сообщение для проверки роутера.

Вам необходимо:
Создать APIRouter с префиксом /notes и тегом notes для группировки эндпоинтов
в документации FastAPI.

Реализовать эндпоинт, который принимает GET-запрос по пути / (итоговый путь:
/notes/). Эндпоинт должен возвращать строку "Notes API is working".
Убедиться, что APIRouter правильно настроен, но не требуется создавать
подключение к основному приложению FastAPI в рамках этой задачи.
"""

from fastapi import APIRouter, status

notes_router = APIRouter(prefix='/notes', tags=['notes'])


@notes_router.get('/', status_code=status.HTTP_200_OK)
def get_notes() -> str:
    return 'Notes API is working'
