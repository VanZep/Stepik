"""
На вход программе подаются названия городов, каждое с новой строки. Необходимо
в цикле читать эти названия, пока не встретится строка "q". С помощью множества
определить общее уникальное число городов, которые читались в программе
(за исключением "q"). На экран вывести это число.

P.S. Из коллекций при реализации программы использовать только множества.

Sample Input:
Уфа
Москва
Тверь
Екатеринбург
Томск
Уфа
Москва
q

Sample Output:
5
"""


def func_1():
    """1-ое решение."""
    unique_cities = set()
    for city in iter(input, 'q'):
        unique_cities.add(city)
    print(len(unique_cities))


def func_2():
    """2-ое решение."""
    city, unique_cities = input(), set()
    while city != 'q':
        unique_cities.add(city)
        city = input()
    print(len(unique_cities))


def func_3():
    """3-е решение."""
    print(len(set(iter(input, 'q'))))


if __name__ == '__main__':
    func_1()
    print()
    func_2()
    print()
    func_3()
