"""
Создайте приложение FastAPI, которое использует библиотеку loguru для
логирования информации о входящих запросах, включая их параметры пути и
HTTP-метод.

Используйте библиотеку loguru для настройки логирования в файл requests.log.
Настройте logger.add() для записи логов в файл requests.log с уровнем INFO.

Реализуйте эндпоинт GET /greet/{username}, который:
Принимает параметр пути username и возвращает JSON-ответ
{"greeting": "Hello, {username}!"}.
Логирует запрос с сообщением в формате: Received {method} request to
/greet/{username} с уровнем INFO.

Создайте функцию log_user_greeting(username: str), которая:
Вызывается внутри эндпоинта GET /greet/{username} и логирует сообщение
Greeted user: {username} с уровнем DEBUG.
Настройте CORS с использованием CORSMiddleware для поддержки запросов с
источников http://localhost:8000, https://mysite.com, null, методов GET,
заголовков Content-Type, с поддержкой учётных данных.
"""

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "https://mysite.com", "null"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type"]
)

logger.add("requests.log", level="INFO")


@app.get(
    "/greet/{username}",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def greeting(request: Request, username: str):
    log_user_greeting(username)
    logger.info(f"Received {request.method} request to {request.url.path}")
    return {"greeting": f"Hello, {username}!"}


def log_user_greeting(username: str):
    logger.debug(f"Greeted user: {username}")
