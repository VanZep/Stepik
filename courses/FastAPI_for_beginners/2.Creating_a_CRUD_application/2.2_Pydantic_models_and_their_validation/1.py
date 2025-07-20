"""
Напишите Pydantic модель для представления пользователя, со следующими полями:
Поле id типа int, обязательное поле.
Поле username типа str, обязательное поле.
Поле email типа EmailStr, обязательное поле.
Поле first_name типа str, не обязательное поле. Если значение не предоставлено,
оно будет равно None.
Поле last_name типа str, не обязательное поле. Если значение не предоставлено,
оно будет равно None.
"""

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
