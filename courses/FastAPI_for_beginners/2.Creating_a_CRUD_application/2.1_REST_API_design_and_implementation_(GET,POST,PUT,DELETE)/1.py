"""
Необходимо создать простой REST API на FastAPI для управления списком
заметок (To-Do).

API должен поддерживать обработку GET запросов, а именно обрабатывать операцию
получения списка всех заметок и получение информации о конкретной заметке
по её ID.

GET /todos/: Получение всех заметок. Возвращает словарь заметок.
GET /todos/{todo_id}: Получение информации о конкретной заметке по ID.
Возвращает текст заметки.

Все заметки хранятся в словаре:
todo_db = {0: "The first note"}
"""

import uvicorn
from fastapi import FastAPI, exceptions

todo_db = {0: "The first note"}

app = FastAPI()


@app.get('/todos')
async def get_todo_list() -> dict:
    return todo_db


@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int) -> str:
    return todo_db.get(todo_id, 'Invalid ID')


if __name__ == '__main__':
    uvicorn.run(app)
