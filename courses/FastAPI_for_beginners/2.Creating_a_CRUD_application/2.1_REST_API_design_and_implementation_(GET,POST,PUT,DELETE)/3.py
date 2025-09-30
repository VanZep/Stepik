"""
Создайте приложение с эндпоинтом для создания напоминания. Напоминания
хранятся в словаре reminders_db (формат id: reminder).

Эндпоинт:
POST /reminders — создаёт напоминание с текстом из Body(...), присваивая id
(максимальный + 1 или 0, если словарь пуст). После успешного создания
напоминания необходимо вернуть строку "Reminder created!" с кодом ответа 201.

Пример: POST /reminders "Meeting at 3 PM" → "Reminder created!".
"""

from fastapi import FastAPI, Body, status

app = FastAPI()

reminders_db = {}


@app.post('/reminders', status_code=status.HTTP_201_CREATED)
async def create_remind(reminder: str = Body(...)) -> str:
    reminders_db[max(reminders_db) + 1 if reminders_db else 0] = reminder
    return 'Reminder created!'
