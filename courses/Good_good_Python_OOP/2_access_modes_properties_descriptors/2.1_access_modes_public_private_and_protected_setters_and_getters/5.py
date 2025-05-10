"""
Объявите в программе два класса Point и Rectangle. Объекты первого класса
должны создаваться командой:
pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа).
При этом в объектах класса Point должны формироваться следующие локальные
свойства:
__x, __y - координаты точки на плоскости.
и один геттер:
get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или
r2 = Rectangle(x1, y1, x2, y2)

Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата
(x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне
зависимости от способа их создания) должны формироваться следующие локальные
свойства:
__sp - объект класса Point с координатами x1, y1 (верхний левый угол)
__ep - объект класса Point с координатами x2, y2 (нижний правый угол)

Также к классе Rectangle должны быть реализованы следующие методы:
set_coords(self, sp, ep) - изменение текущих координат, где sp, ep -
объекты класса Point
get_coords(self) - возвращение кортежа из объектов класса Point с текущими
координатами прямоугольника (ссылки на локальные свойства __sp и __ep)
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами:
(x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения
координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
"""


class Point:

    def __init__(self, x, y):
        self.__x = self.__y = None

        if self.check_coords(x, y):
            self.__x = x
            self.__y = y

    @staticmethod
    def check_coords(x, y):
        return type(x) in (int, float) and type(y) in (int, float)

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, a, b, c=None, d=None):
        if isinstance(a, Point) and isinstance(b, Point):
            self.set_coords(a, b)
        else:
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(
            'Прямоугольник с координатами: '
            f'{self.__sp.get_coords()} {self.__ep.get_coords()}'
        )


rect_1 = Rectangle(Point(0, 0), Point(20, 34))
rect_2 = Rectangle(1, 2, 3, 4)
rect_1.draw()
rect_2.draw()
