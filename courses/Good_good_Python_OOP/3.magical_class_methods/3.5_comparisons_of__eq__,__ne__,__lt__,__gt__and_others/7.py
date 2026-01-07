"""
Необходимо объявить класс Body (тело), объекты которого создаются командой:
body = Body(name, ro, volume)
где name - название тела (строка)
ro - плотность тела (число: вещественное или целочисленное)
volume - объем тела (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:
body1 > body2 # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10 # True, если масса тела body1 меньше 10
body2 == 5 # True, если масса тела body2 равна 5

Масса тела вычисляется по формуле:
m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""

from __future__ import annotations


class Body:

    def __init__(
            self,
            name: str,
            ro: int | float,
            volume: int | float
    ) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self) -> float:
        return self.ro * self.volume

    def __eq__(self, other: int | Body) -> bool:
        self.check_other(other)
        other_weight = other.get_weight() if isinstance(other, Body) else other

        return self.get_weight() == other_weight

    def __lt__(self, other: int | Body) -> bool:
        self.check_other(other)
        other_weight = other.get_weight() if isinstance(other, Body) else other

        return self.get_weight() < other_weight

    @staticmethod
    def check_other(other: int | Body) -> None:
        if type(other) != int and not isinstance(other, Body):
            raise TypeError('Объектом сравнения должен быть Body или int')
