"""
Напишите программу, которая с помощью модуля random генерирует случайный
пароль. Программа принимает на вход длину пароля и выводит случайный пароль,
содержащий только символы английского алфавита a..z, A..Z
(в нижнем и верхнем регистре).
"""

import string
import random

length = int(input())

password = ''.join(
    [random.choice(string.ascii_letters) for _ in range(length)]
)
print(password)
