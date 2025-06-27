"""
Напишите функцию mean(), которая принимает произвольное количество аргументов
и возвращает среднее арифметическое переданных в нее числовых (int или float)
аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список,
а именно произвольное количество аргументов.

Примечание 2. Функция должна игнорировать аргументы всех типов,
кроме int или float.

Примечание 3. Приведенный ниже код:
print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

должен выводить:
0.0
7.0
2.0
0.0
3.5
5.5
"""


def mean(*args):
    numbers = [num for num in args if type(num) in (int, float)]
    return sum(numbers) / (len(numbers) or 1)


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
