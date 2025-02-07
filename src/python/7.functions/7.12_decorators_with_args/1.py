"""
На вход программе подаются целые числа, записанные через пробел. Прочитайте
эту строку и сохраните через какую-либо переменную.

Напишите функцию, которая имеет один параметр, преобразовывает переданную ей
строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start -
начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную
функцию для прочитанной строки. Результат (сумму) отобразите на экране.

Sample Input:
5 6 3 6 -4 6 -1

Sample Output:
26
"""
from functools import wraps


def increases_by(start=0):
    """Декоратор. Увеличивает значение на величину start."""

    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper

    return decorator_func


@increases_by(start=5)
def make_list(string):
    """Преобразовывает строку string в список чисел и возвращает их сумму."""
    return sum(map(int, string.split()))


if __name__ == '__main__':
    nums_str = input()
    print(make_list(nums_str))
