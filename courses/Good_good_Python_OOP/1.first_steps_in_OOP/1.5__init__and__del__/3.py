"""
Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть
возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)

Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого
и нижнего левого углов (произвольные числа). В каждом объекте координаты
должны сохраняться в локальных свойствах sp (верхний правый угол) и ep
(нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс
выбирается случайно (или Line, или Rect, или Ellipse). Координаты также
генерируются случайным образом (числовые значения). Все объекты сохраните
в списке elements.

В списке elements обнулите координаты объектов только для класса Line.
"""

from random import randint, choice


class Line:

    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:

    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:

    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


def choose_random_class():
    return choice((Line, Rect, Ellipse))


def choose_random_coords(min_lim, max_lim):
    return (
        randint(min_lim, max_lim), randint(min_lim, max_lim),
        randint(min_lim, max_lim), randint(min_lim, max_lim)
    )


elements = [
    choose_random_class()(*choose_random_coords(0, 10)) for _ in range(217)
]

for el in elements:
    if el.__class__ == Line:
        el.sp = 0, 0
        el.ep = 0, 0

    print(el.__class__, el.sp, el.ep)
