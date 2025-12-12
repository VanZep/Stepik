"""
Создайте приложение FastAPI с кастомным промежуточным программным обеспечением
(Middleware) на основе функций, которое выводит путь запроса с текущим
временем в формате ISO 8601.

Используйте декоратор @app.middleware("http") для создания функции
промежуточного программного обеспечения.

Реализуйте функцию Middleware, которая:
Получает текущее время с помощью модуля datetime в формате ISO 8601 (например,
2025-09-05T09:11:00Z, разделитель буква T).
Выведите путь запроса в консоль в формате: {request_time} - Processed request
to {path}.
Создайте эндпоинт GET /welcome — возвращает JSON-ответ
{"message": "Welcome to the API"}.
Используйте класс Request из fastapi для получения пути запроса
(request.url.path).
Настройте CORS с использованием CORSMiddleware для поддержки запросов с
источников http://localhost:8000, https://myapp.com, null, методов GET,
заголовков Content-Type, с поддержкой учётных данных.
"""

from datetime import datetime

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000', 'https://myapp.com', 'null'],
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['Content-Type']
)


@app.middleware('http')
async def get_request_path_middleware(request: Request, call_next):
    request_time = datetime.now().isoformat()
    print(f'{request_time} - Processed request to {request.url.path}')
    return await call_next(request)


@app.get(
    '/welcome',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def greeting():
    return {'message': 'Welcome to the API'}
