"""
На вход программе подаются строки (пункты меню), каждая с новой строки,
в формате:
название_1 URL-адрес_1
название_2 URL-адрес_2
...
название_N URL-адрес_N

В программе уже реализовано чтение этих строк и сохранение их в списке:
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
'Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php'
]

Необходимо преобразовать список lst_in так, чтобы получился кортеж menu
следующего вида:
((название_1, URL-адрес_1), (название_2, URL-адрес_2),
... (название_N, URL-адрес_N))

Полученный кортеж вывести на экран командой:
print(menu)

Sample Input:
Главная home
Python learn-python
Java learn-java
PHP learn-php

Sample Output:
(('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'),
('PHP', 'learn-php'))
"""

lst_in = [
    'Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php'
]


def func():
    """Решение."""
    menu = tuple(tuple(i.split()) for i in lst_in)
    print(menu)


if __name__ == '__main__':
    func()
