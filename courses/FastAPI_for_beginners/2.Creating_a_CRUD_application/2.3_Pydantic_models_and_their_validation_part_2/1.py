"""
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт
для получения списка задач с использованием Pydantic модели для ответа. У вас
есть глобальный in-memory список tasks для хранения объектов. Эндпоинт должен
возвращать весь список tasks в формате моделей.

Вам необходимо:
Определить Pydantic модель Task с полями id: int, title: str, completed: bool.

Реализовать эндпоинт, который принимает GET запрос по пути /tasks. Он должен
возвращать весь список tasks в формате List[Task]. То есть ответ эндпоинта
должен быть следующий: JSON со списком задач в формате List[Task].

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать
ошибок при запуске приложения.
"""

from pydantic import BaseModel
from fastapi import FastAPI, status

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False)
]


@app.get('/tasks', status_code=status.HTTP_200_OK, response_model=list[Task])
async def get_all_tasks() -> list[Task]:
    return tasks
