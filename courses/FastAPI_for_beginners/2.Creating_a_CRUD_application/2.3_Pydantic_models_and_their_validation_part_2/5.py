"""
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт
для удаления заметки. У вас есть глобальный список notes для хранения заметок.
Эндпоинт должен удалять заметку из списка notes по ID и возвращать удалённую
модель.

Вам необходимо:
Определить Pydantic модель Note с полями id: int, text: str.

Реализовать эндпоинт, который принимает DELETE запрос по пути /notes/{note_id}.
Он будет принимать note_id как параметр пути, удалять соответствующую заметку
из списка notes и возвращать удалённую модель Note. Если заметка не найдена,
выбросить HTTP-ошибку 404 с сообщением "Note not found".
То есть ответ эндпоинта должен быть следующий: JSON с данными удалённой заметки
в формате модели Note (например, {"id": 1, "text": "Удалённая заметка"}).

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать
ошибок при запуске приложения.
"""

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


class Note(BaseModel):
    id: int
    text: str


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]


@app.delete(
    '/notes/{note_id}',
    status_code=status.HTTP_200_OK,
    response_model=Note
)
async def delete_note(note_id: int) -> Note:
    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            return note

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Note not found'
    )
