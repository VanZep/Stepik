"""
Создайте приложение FastAPI с поддержкой двух версий API, используя
URL-префиксы для разделения версий.

Реализуйте основное приложение FastAPI и два подприложения для версий v1 и v2.
Настройте подприложения с кастомными заголовками и описаниями:
v1: title="API Version 1", description="First version of the API".

v2: title="API Version 2", description="Second version of the API with updated
features".

Реализуйте эндпоинт GET /users для каждого подприложения:
В v1: возвращает JSON-ответ {"version": "v1", "users": ["Alice", "Bob"]}.

В v2: возвращает JSON-ответ {
    "version": "v2", "users": ["Alice", "Bob", "Charlie"]
}.

Используйте метод app.mount() для монтирования подприложений по путям
/v1 и /v2.
"""

from fastapi import FastAPI, status

app = FastAPI()
app_v1 = FastAPI(title="API Version 1", description="First version of the API")
app_v2 = FastAPI(
    title="API Version 2",
    description="Second version of the API with updated features"
)


@app_v1.get(
    "/users",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def get_users_v1():
    return {"version": "v1", "users": ["Alice", "Bob"]}


@app_v2.get(
    "/users",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def get_users_v2():
    return {"version": "v2", "users": ["Alice", "Bob", "Charlie"]}


app.mount("/v1", app_v1)
app.mount("/v2", app_v2)
