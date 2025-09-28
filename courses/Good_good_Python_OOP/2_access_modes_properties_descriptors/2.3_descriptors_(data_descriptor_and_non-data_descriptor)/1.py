"""
Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал
вещественные значения. При записи вещественного числа должна выполняться
проверка на вещественный тип данных. Если проверка не проходит, то
генерировать исключение командой:
raise TypeError("Присваивать можно только вещественный тип данных.")

Объявите класс Cell, в котором создается объект value дескриптора FloatValue.
А объекты класса Cell должны создаваться командой:
cell = Cell(начальное значение ячейки)

Объявите класс TableSheet, с помощью которого создается таблица из N строк и
M столбцов следующим образом:
table = TableSheet(N, M)

Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
работать с вещественными числами через объект value (начальное значение должно
быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:
cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты
класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку, построчно).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_float(value)
        setattr(instance, self.name, value)

    @staticmethod
    def verify_float(value):
        if not isinstance(value, float):
            raise TypeError(
                'Присваивать можно только вещественный тип данных.'
            )


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, width, height):
        self.cells = [[Cell() for _ in range(height)] for _ in range(width)]

    def fill_table(self, start):
        for row in self.cells:
            for cell in row:
                cell.value = float(start)
                start += 1


table = TableSheet(5, 3)
table.fill_table(1)
for row in table.cells:
    for cell in row:
        print(cell.value)
