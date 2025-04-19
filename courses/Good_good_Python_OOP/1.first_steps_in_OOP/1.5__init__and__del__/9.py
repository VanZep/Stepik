"""
Объявите два класса:
Cell - для представления клетки игрового поля
GamePole - для управления игровым полем, размером N x N клеток

С помощью класса Cell предполагается создавать отдельные клетки командой:
c1 = Cell(around_mines, mine)

Здесь around_mines - число мин вокруг данной клетки поля;
mine - булева величина (True/False), означающая наличие мины в текущей клетке.
При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие/отсутствие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False).
Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое
поле с числом клеток N x N:
pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка
представляется объектом класса Cell и все объекты хранятся в двумерном списке
N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:
init() - инициализация поля с новой расстановкой M мин (случайным образом по
игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если
клетка не открыта, то отображается символ #; мина отображается символом *;
между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать
метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и
числом мин M = 12.
"""

import random


class Cell:

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = self.init()

    def init(self):
        pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]
        self.set_mines(pole)
        self.set_nums(pole)
        return pole

    def set_mines(self, pole):
        mines = self.m
        while mines:
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            if not pole[i][j].mine:
                pole[i][j].mine = True
                mines -= 1

    def set_nums(self, pole):
        indx = (
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)
        )
        for i in range(self.n):
            for j in range(self.n):
                if not pole[i][j].mine:
                    pole[i][j].around_mines = sum(
                        pole[i + x][j + y].mine for x, y in indx if
                        0 <= i + x < self.n and 0 <= j + y < self.n
                    )

    def show(self):
        pole = [[None] * (self.n) for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine and self.pole[i][j].fl_open:
                    pole[i][j] = '*'
                elif not self.pole[i][j].fl_open:
                    pole[i][j] = '#'
                else:
                    pole[i][j] = self.pole[i][j].around_mines

        for row in pole:
            print(*row)


if __name__ == '__main__':
    N = 10
    M = 12
    pole_game = GamePole(N, M)
    pole_game.show()
