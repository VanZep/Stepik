"""
Создайте приложение FastAPI с поддержкой CORS (Cross-Origin Resource Sharing)
для обработки запросов от внешних клиентов, работающих на разных доменах.

Используйте CORSMiddleware из модуля fastapi.middleware.cors для настройки
CORS.
Настройте CORS, чтобы разрешить доступ к API только с источников:
http://localhost:8000, https://myapp.com и локальных файлов (null).
Разрешите использование HTTP-методов GET и POST.
Разрешите передачу HTTP-заголовков Authorization и Content-Type в запросах.
Включите поддержку отправки учётных данных (credentials) в запросах.
Создайте эндпоинт /data с помощью декоратора @app.get, который принимает
GET-запрос и возвращает JSON-ответ {"data": "CORS configured successfully"}.
"""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000', 'https://myapp.com', 'null'],
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['Authorization', 'Content-Type']
)


@app.get(
    '/data',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def get_data():
    return {'data': 'CORS configured successfully'}
