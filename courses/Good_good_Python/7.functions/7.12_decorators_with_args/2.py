"""
Объявите функцию, которая переводит символы строки в нижний регистр
(малые буквы) и возвращает результат.
Определите декоратор для этой функции, который имеет один параметр tag,
определяющий строку с названием тега и начальным значением "h1". Этот
декоратор должен заключать возвращенную функцией строку в тег tag
и возвращать результат.

Пример заключения строки "python" в тег h1:
<h1>python</h1>

Примените декоратор со значением tag="div" к функции и вызовите декорированную
функцию для строки s, прочитанной из входного потока:
s = input()

Результат работы декорированной функции отобразите на экране.

Sample Input:
Декораторы - это классно!

Sample Output:
<div>декораторы - это классно!</div>
"""
from functools import wraps


def wraps_in_tag(tag='h1'):
    """Декоратор. Заключает строку в тег tag."""

    def func_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return func_decorator


@wraps_in_tag(tag='div')
def get_lower_string(string):
    """Переводит символы строки в нижний регистр и возвращает результат."""
    return string.lower()


if __name__ == '__main__':
    s = input()
    print(get_lower_string(s))
