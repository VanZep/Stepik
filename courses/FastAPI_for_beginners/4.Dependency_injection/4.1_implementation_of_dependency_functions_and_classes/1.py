"""
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт
/welcome с использованием механизма зависимостей. Эндпоинт должен возвращать
JSON-объект, содержащий фиксированное сообщение, предоставленное зависимостью.

Вам необходимо:
1. Определить зависимость get_message, возвращающую фиксированную строку
"Hello from dependency!"

2. Реализовать эндпоинт который принимает метод GET по пути /welcome. Он должен
использовать зависимость get_message и возвращать JSON-объект с ключом
"message" и значением, полученным от зависимости.
То есть ответ эндпоинта должен быть следующий: JSON-объект вида
{"message": значение_зависимости}, где значение_зависимости — строка,
возвращённая функцией get_message.
"""

from fastapi import FastAPI, Depends, status

app = FastAPI()


def get_message() -> str:
    return 'Hello from dependency!'


@app.get('/welcome', status_code=status.HTTP_200_OK)
def welcome(greeting: str = Depends(get_message)) -> dict[str, str]:
    return {'message': greeting}
