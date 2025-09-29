"""
Создайте приложение с эндпоинтом для чтения всех заметок. Заметки должны
хранится в словаре notes_db, где ключ — id (целое число), значение — content
(строка).

Эндпоинт:
GET /notes — возвращает словарь всех заметок. Если словарь пуст, возвращает {}.

Пример: GET /notes → {0: "Study FastAPI", 1: "I like FastAPI"}.
"""

from fastapi import FastAPI

app = FastAPI()

notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}


@app.get('/notes')
async def get_notes() -> dict:
    return notes_db
