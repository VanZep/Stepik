"""
Почтовый индекс в Латверии имеет вид:
LetterLetterNumber_NumberLetterLetter
где Letter – заглавная буква английского алфавита, Number – число от 0 до
99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует
и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:
AB23_56VG          # правильный
V3F_231GT          # неправильный
"""

from random import choices, randrange
from string import ascii_uppercase


def generate_index():
    def gen_4_chars():
        return ''.join(choices(ascii_uppercase, k=2) + [str(randrange(100))])

    return f'{gen_4_chars()}_{gen_4_chars()[::-1]}'


print(generate_index())
