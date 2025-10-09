"""
Объявите в программе класс Dimensions (габариты) с атрибутами:
MIN_DIMENSION = 10
MAX_DIMENSION = 1000

Каждый объект класса Dimensions должен создаваться командой:
d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры

и содержать локальные атрибуты:
__a, __b, __c - габаритные размеры (целые или вещественные числа)

Для работы с этими локальными атрибутами в классе Dimensions следует прописать
следующие объекты-свойства:
a, b, c - для изменения и считывания соответствующих локальных
атрибутов __a, __b, __c

При изменении значений __a, __b, __c следует проверять, что присваиваемое
значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так,
то новое значение не присваивается (игнорируется).

С помощью магических методов данного занятия запретить создание локальных
атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При
попытке это сделать генерировать исключение:
raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

Пример использования класса (эти строчки в программе писать не нужно):
d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError


P.S. В программе нужно объявить только класс Dimensions. На экран ничего
выводить не нужно.
"""

from typing import Union


class Dimensions:
    __a: Union[int, float]
    __b: Union[int, float]
    __c: Union[int, float]

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError(
                'Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.'
            )

        if key in self.__annotations__ and (
                not isinstance(value, self.__annotations__.get(key))
        ):
            raise TypeError('Неверный тип присваиваемых данных.')

        if not (self.MIN_DIMENSION <= value <= self.MAX_DIMENSION):
            return

        super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b, c)
d.MAX_DIMENSION = 10  # исключение AttributeError
