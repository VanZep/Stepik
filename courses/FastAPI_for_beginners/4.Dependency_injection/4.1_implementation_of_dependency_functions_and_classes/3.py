"""
Разработайте веб-приложение на фреймворке FastAPI, которое реализует
защищённый эндпоинт /profile с использованием механизма зависимостей. Эндпоинт
должен проверять токен и возвращать сообщение "User is authorized" при
успешной авторизации, иначе выбрасывать HTTPException с кодом 401.

Вам необходимо:
1. Определить зависимость check_auth, принимающую параметр token типа str через
параметр запроса и возвращающую True, если полученный token равен "secret",
иначе выбрасывающую HTTPException с кодом 401 и сообщением "Unauthorized".

2. Реализовать эндпоинт, который принимает GET запрос по пути /profile. Он
будет использовать зависимость check_auth и возвращать строку
"User is authorized" при успешной проверке. То есть ответ эндпоинта должен
быть следующий: строка "User is authorized", если токен валиден, иначе
HTTP-ошибка 401 с сообщением "Unauthorized".
"""

from typing import Union

from fastapi import FastAPI, HTTPException, status, Depends, Query

app = FastAPI()


def check_auth(token: str = Query(...)) -> Union[bool, HTTPException]:
    if token != 'secret':
        raise HTTPException(
            detail='Unauthorized',
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    return True


@app.get('/profile', status_code=status.HTTP_200_OK)
def profile(is_auth: bool = Depends(check_auth)) -> str:
    return 'User is authorized'
