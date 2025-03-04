"""
Объявите в программе функцию с именем get_list_digследующей сигнатуры:
def get_list_dig(lst): ...

Функция должна возвращать список только из числовых значений переданной ей
коллекции (список или кортеж).
"""


def get_list_dig(lst):
    """Возвращает список только из числовых
    значений переданной ей коллекции.
    """
    return list(filter(
        lambda x:
            isinstance(x, int) and not
            isinstance(x, bool) or
            isinstance(x, float),
        lst))


print(get_list_dig([1, 2, 3.2, 4, "a", True, [4, 5], "c", (4, 5)]))
print(get_list_dig({5, 6, 7, '8.1', 5.5, '4'}))
print(get_list_dig((10, "f", '33', True, 12)))
print(get_list_dig(['1', True, False, (1, 23)]))
