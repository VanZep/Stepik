"""
Объявите в программе функцию с именем get_add следующей сигнатуры:
def get_add(a, b): ...
Функция должна складывать или два числа или две строки (но не число со строкой)
и возвращать полученный результат. Если сложение не может быть выполнено, то
функция возвращает значение None.
"""


def get_add(a, b):
    """Складывает или два числа или две строки."""
    if (
            type(a) in (int, float) and type(b) in (int, float)
            or
            isinstance(a, str) and isinstance(b, str)
    ):
        return a + b
    return None


print(get_add(True, 1))
