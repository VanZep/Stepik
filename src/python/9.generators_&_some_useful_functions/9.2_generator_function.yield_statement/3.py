"""
На вход программе подается натуральное число N (N > 8). Необходимо его
прочитать и объявить функцию-генератор, которая бы выдавала пароль длиной N
символов из случайных букв, цифр и некоторых других знаков. Значение N
передается в функцию-генератор первым аргументом. Для получения
последовательности допустимых символов для генерации паролей в программе
импортированы две строки: ascii_lowercase, ascii_uppercase, на основе которых
формируется общий список:
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

Функция-генератор должна при каждом вызове возвращать новый пароль из случайно
выбранных символов chars длиной N и делать это бесконечно, то есть, вызывать
ее можно бесконечное число раз.

Сгенерируйте с помощью функции-генератора первые пять паролей и выведите их в
столбик (каждый с новой строки).

Подсказка: сгенерировать случайный индекс indx в диапазоне [a; b] для выбора
символа из chars можно с помощью функции randint модуля random:
import random
random.seed(1)
indx = random.randint(a, b)

Sample Input:
10

Sample Output:
riGp?58WAm
!dX3a5IDnO
dcdbWB2d*C
4?DSDC6Lc1
mxLpQ@2@yM
"""

from random import randint, seed
from string import ascii_lowercase, ascii_uppercase

seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def get_random_psw(length):
    """Функция-генератор. Возвращает случайный пароль длинной length."""
    while True:
        psw = ''
        for i in range(length):
            psw += chars[randint(0, len(chars) - 1)]
        yield psw


if __name__ == '__main__':
    N = int(input())
    gen = get_random_psw(N)
    for _ in range(5):
        print(next(gen))
