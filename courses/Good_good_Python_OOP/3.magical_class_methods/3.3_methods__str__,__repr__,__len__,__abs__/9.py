"""
Объявите класс PolyLine (полилиния) для представления линии из
последовательности прямолинейных сегментов. Объекты этого класса должны
создаваться командой:
poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)

Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y);
coord_2, coord_3, ... - последующие координаты точек на плоскости
(представленные кортежами), соединенных прямыми линиями.

Например:
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))

В классе PolyLine должны быть объявлены следующие методы:
add_coord(x, y) - добавление новой координаты (в конец);
remove_coord(indx) - удаление координаты по индексу (порядковому номеру,
начинается с нуля);
get_coords() - получение списка координат (в виде списка из кортежей).

P.S. На экран ничего выводить не нужно, только объявить класс.
"""


class PolyLine:

    def __init__(self, *args):
        self.__coords = []
        self.__coords = list(args)

    def add_coord(self, x, y):
        if self.__verify_coord((x, y)):
            self.__coords.append((x, y))

    def remove_coord(self, indx):
        if 0 <= indx < len(self.__coords):
            self.__coords.pop(indx)

    def get_coords(self):
        return self.__coords

    def __setattr__(self, key, value):
        if all(self.__verify_coord(item) for item in value):
            return super().__setattr__(key, value)

    @staticmethod
    def __verify_coord(coord):
        return (
                isinstance(coord, tuple)
                and len(coord) == 2
                and isinstance(coord[0], (int, float))
                and isinstance(coord[1], (int, float))
        )


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(9, 0)
print(poly.get_coords())
