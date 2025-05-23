"""
Объявите класс Line для описания линии на плоскости, объекты которого
предполагается создавать командой:
line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные
свойства:
__x1, __y1 - начальная координата
__x2, __y2 - конечная координата

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:
set_coords(self, x1, y1, x2, y2) - для изменения координат линии
get_coords(self) - для получения кортежа из текущих координат линии

А также метод:
draw(self) - для отображения в консоли списка текущих координат линии (в одну
строчку через пробел)
"""


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)

    @staticmethod
    def check_coords(*coords):
        checks = []
        for coord in coords:
            checks.append(isinstance(coord, (int, float)))

        return all(checks)

    def set_coords(self, x1, y1, x2, y2):
        if self.check_coords(x1, y1, x2, y2):
            self.__x1 = x1
            self.__y1 = y1
            self.__x2 = x2
            self.__y2 = y2
        else:
            raise TypeError(
                'Координаты должны быть целыми числами или '
                'числами с плавющей точкой.'
                )

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


line = Line(1.1, 2.2, 10, 20)
line.draw()
