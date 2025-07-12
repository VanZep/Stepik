"""
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с
именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары
имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:
Aaron
Abdul
Abe
Abel
Abraham
Albert

и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein

то результатом могло быть:
Abdul Albertson
Abel Adamson
Albert Einstein
"""

from random import choice

with (
    open('first_names.txt') as f_names,
    open('last_names.txt') as l_names
):
    first_names, last_names = f_names.read().split(), l_names.read().split()

print(
    *(f'{choice(first_names)} {choice(last_names)}' for _ in range(3)),
    sep='\n'
)
