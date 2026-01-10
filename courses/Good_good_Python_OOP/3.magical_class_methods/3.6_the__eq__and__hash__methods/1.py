"""
Объявите в программе класс с именем Rect (прямоугольник), объекты которого
создаются командой:
rect = Rect(x, y, width, height)
где x, y - координата верхнего левого угла (числа: целые или вещественные)
width, height - ширина и высота прямоугольника (числа: целые или вещественные).

В этом классе определите магический метод, чтобы хэши объектов класса Rect с
равными width, height были равны. Например:
r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2

P.S. На экран ничего выводить не нужно, только объявить класс.
"""

Digit = int | float


class Rect:

    def __init__(
            self,
            x: Digit,
            y: Digit,
            width: Digit,
            height: Digit
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __setattr__(self, key, value) -> None:
        self.int_float_validator(value)
        super.__setattr__(self, key, value)

    def __hash__(self) -> int:
        return hash((self.width, self.height))

    @staticmethod
    def int_float_validator(value) -> None:
        if not isinstance(value, float) and type(value) != int:
            raise TypeError('Неверный тип данных')


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2
print(h1 == h2)
