"""
Объявите в программе функцию с именем get_data_fig для вычисления периметра
произвольного N-угольника. На вход этой функции передаются N длин сторон
через ее аргументы. Дополнительно могут быть указаны именованные аргументы:
- tp - булево значение True/False
- color - целое числовое значение
- closed - булево значение True/False
- width - вещественное значение
Функция должна возвращать в виде кортежа периметр многоугольника и указанные
значения именованных параметров в порядке их перечисления в тексте задания
(если они были переданы). Если какой-либо параметр отсутствует, его возвращать
не нужно (пропустить).

Sample Input:
1 2 3 4 3 2 4

Sample Output:
19
19 True
19 True 7
19 False 2.0
"""


def get_data_fig(*args, **kwargs):
    """Вычисляет периметр произвольного N-угольника."""
    extra_args = ('tp', 'color', 'closed', 'width')
    return sum(args), *(kwargs.get(i) for i in extra_args if i in kwargs)


if __name__ == '__main__':
    num_list = list(map(int, input().split()))
    print(*get_data_fig(*num_list))
    print(*get_data_fig(*num_list, tp=True))
    print(*get_data_fig(*num_list, tp=True, color=7))
    print(*get_data_fig(*num_list, closed=False, width=2.0))
