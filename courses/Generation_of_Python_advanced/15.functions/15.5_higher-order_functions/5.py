"""
Напишите функцию func_apply(), принимающую на вход функцию и список значений и
возвращающую список, в котором каждое значение будет результатом применения
переданной функции к переданному списку.

Примечание 1. При условии, что функция func_apply() написана правильно,
приведенный ниже код:
def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))

должен выводить:
[7, 14, 21, 28, 35, 42]
[4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6']
"""


def func_apply(func, lst):
    return list(map(func, lst))


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))
