"""
Объявите в программе функцию с именем get_sq, которая имеет один параметр
(принимает вещественное число). В теле функции значение параметра возводится
в квадрат и возвращается функцией.

После объявления функции прочитайте (с помощью функции input) вещественное
число из входного потока и вызовите функцию с прочитанным значением. Выведите
на экран число, которое возвратила функция.

Sample Input:
1.5

Sample Output:
2.25
"""

number = float(input())


def get_sq(num):
    """Возводит значение в квадрат."""
    return num ** 2


if __name__ == '__main__':
    print(get_sq(number))
