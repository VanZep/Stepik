"""
Объявите в программе функцию с именем get_rect_value, которая первыми двумя
параметрами принимает длину и ширину прямоугольника (числа), а третий
формальный параметр tp имеет начальное значение 0. Если параметр tp равен нулю,
то функция должна возвращать периметр прямоугольника, вычисленного на основе
первых двух переданных аргументов, а иначе его площадь.
"""


def get_rect_value(length, width, tp=0):
    """Если параметр tp равен нулю, то функция возвращает периметр
    прямоугольника, вычисленного на основе первых двух переданных
    аргументов, а иначе его площадь.
    """
    return length * width if tp else (length + width) * 2


def test_get_rect_value(func):
    """Тест функции get_rect_value ."""
    length, width, tp = 2, 3, True
    result_1 = 10
    result_2 = 6
    if func(length, width) == result_1 and func(length, width, tp) == result_2:
        print('Test "get_rect_value" - OK')
    else:
        print('Test "get_rect_value" - FAILED')


if __name__ == '__main__':
    test_get_rect_value(get_rect_value)
