"""
На вход программе подается натуральное число N, которое необходимо прочитать и
сохранить через переменную. Используя строки из латинских букв ascii_lowercase
и ascii_uppercase:
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
объявите функцию-генератор с одним параметром max_size, которая бы возвращала
случайно сформированные email-адреса с доменом mail.ru и длиной max_size = N
символов. Например, при N=6 адрес может выглядеть так: SCrUZo@mail.ru

Функция-генератор должна возвращать бесконечное число таких адресов, то есть,
генерировать постоянно. Выведите первые пять сгенерированных email и выведите
их в столбик (каждый с новой строки).

Подсказка: для формирования случайного индекса для выбора символа из строки
chars, используйте функцию randint модуля random:
import random
random.seed(1)
indx = random.randint(0, len(chars)-1)

Sample Input:
8

Sample Output:
iKZWeqhF@mail.ru
WCEPyYng@mail.ru
FbyBMWXa@mail.ru
SCrUZoLg@mail.ru
ubbbPIay@mail.ru
"""

from random import randint, seed
from string import ascii_lowercase, ascii_uppercase

seed(1)
chars = ascii_lowercase + ascii_uppercase


def get_random_email(max_size):
    """Функция-генератор. Возвращает случайный email с доменом mail.ru
    и длинной max_size.
    """
    while True:
        email = ''
        for i in range(max_size):
            email += chars[randint(0, len(chars) - 1)]
        yield f'{email}@mail.ru'


if __name__ == '__main__':
    N = int(input())
    gen = get_random_email(N)
    for _ in range(5):
        print(next(gen))
