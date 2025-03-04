"""
В программе инициализируется двумерное игровое поле размером N x N
(N - натуральное число читается из входного потока), представленное в виде
вложенного списка:
P = [[0] * N for i in range(N)]

Требуется расставить на поле P случайным образом M = 10 единиц (целочисленных)
так, чтобы они не соприкасались друг с другом (то есть, вокруг каждой единицы
должны быть нули, либо граница поля).

Sample Input:
10

Sample Output:
True
"""

from random import randrange, seed
from copy import deepcopy


def expand_pole(pole):
    """Расширяет поле на 1 с каждой стороны."""
    lst = deepcopy(pole)
    lst.append(N * [0])
    lst.insert(0, N * [0])
    for row in lst:
        row.insert(0, 0)
        row.append(0)
    return lst


def is_isolate(i, j):
    """Проверяет изолированность ячейки от других единиц."""
    return sum(
        expanded_P[i][j:j + 3]
        + expanded_P[i + 1][j:j + 3]
        + expanded_P[i + 2][j:j + 3]
    ) == 0


def arrange_units(quantity):
    """Расставляет единицы на поле."""
    while quantity > 0:
        i, j = randrange(N), randrange(N)
        if is_isolate(i, j):
            P[i][j] = 1
            expanded_P[i + 1][j + 1] = 1
            quantity -= 1


if __name__ == '__main__':
    seed(1)
    N = int(input())
    M = 10
    P = [[0] * N for i in range(N)]
    expanded_P = expand_pole(P)
    arrange_units(M)
    print(P)
