"""
Создайте приложение FastAPI, которое поддерживает две версии API, используя
параметр запроса для определения версии.

Реализуйте эндпоинт GET /items/ с параметром запроса version (целое число,
по умолчанию 1).
В зависимости от значения version возвращайте разные JSON-ответы:
Если version == 1: {
    "version": "v1",
    "items": [
        {"id": 1, "name": "Item A"},
        {"id": 2, "name": "Item B"}
    ]
}.

Если version == 2: {
    "version": "v2",
    "items": [
        {"id": 1, "name": "Item A", "price": 10.0},
        {"id": 2, "name": "Item B", "price": 20.0}
    ]
}.

Если version не равен 1 или 2, возвращайте ошибку с кодом 400 и JSON-ответ
{"error": "Invalid version"} (используйте HTTPException).

Настройте основное приложение FastAPI с заголовком title="Items API" и
описанием description="API for retrieving items with versioning".
"""

from fastapi import FastAPI, status, HTTPException

app = FastAPI(
    title="Items API",
    description="API for retrieving items with versioning"
)


@app.get(
    '/items',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def get_items(version: int = 1):
    if version == 1:
        return {
            "version": "v1",
            "items": [
                {"id": 1, "name": "Item A"},
                {"id": 2, "name": "Item B"}
            ]
        }
    elif version == 2:
        return {
            "version": "v2",
            "items": [
                {"id": 1, "name": "Item A", "price": 10.0},
                {"id": 2, "name": "Item B", "price": 20.0}
            ]
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Invalid version"}
        )
