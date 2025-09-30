"""
Создайте FastAPI-приложение для управления комментариями. Комментарии хранятся
в словаре comments_db, где ключ — id (целое число), значение — comment (строка).

Эндпоинты:
GET /comments — возвращает все комментарии (dict).

GET /comments/{comment_id} — возвращает комментарий (str) по comment_id. Если
комментария нет, выводится сообщение "Comment not found"  с кодом ответа 404.

POST /comments — создаёт комментарий с текстом из Body(...), присваивая id
(максимальный существующий + 1 или 0 для пустого словаря). Возвращает "Comment
created!" с кодом ответа 201.

PUT /comments/{comment_id} — обновляет комментарий по comment_id с текстом из
Body(...). Возвращает "Comment updated!". Если комментарий не найден,
выводится сообщение "Comment not found" с кодом ответа 404.

DELETE /comments/{comment_id} — удаляет комментарий по comment_id. Возвращает
"Comment deleted!". Если комментарий не найден, выводится сообщение "Comment
not found" с кодом ответа 404.
"""

from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()
comments_db = {0: "First comment in FastAPI"}


async def validate_id(comment_id):
    if comment_id not in comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Comment not found'
        )


@app.get('/comments', status_code=status.HTTP_200_OK)
async def get_all_comments() -> dict:
    return comments_db


@app.get('/comments/{comment_id}', status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int) -> str:
    await validate_id(comment_id)
    return comments_db[comment_id]


@app.post('/comments', status_code=status.HTTP_201_CREATED)
async def create_comment(comment: str = Body(...)) -> str:
    comments_db[max(comments_db) + 1 if comments_db else 0] = comment
    return 'Comment created!'


@app.put('/comments/{comment_id}', status_code=status.HTTP_200_OK)
async def update_comment(comment_id: int, comment: str = Body(...)) -> str:
    await validate_id(comment_id)
    comments_db[comment_id] = comment
    return 'Comment updated!'


@app.delete('/comments/{comment_id}', status_code=status.HTTP_200_OK)
async def delete_comment(comment_id: int) -> str:
    await validate_id(comment_id)
    comments_db.pop(comment_id)
    return 'Comment deleted!'
