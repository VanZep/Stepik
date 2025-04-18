"""
Объявите в программе следующий двумерный кортеж, размером 5 x 5 элементов:
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
На вход программе подается натуральное число N (N < 5). Необходимо на основе
кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов
путем отбрасывания последних строк и столбцов. Результат выведите на экран в
виде таблицы чисел.

P.S. Обратите внимание, что в при выводе таблицы в конце строк не должно быть
пробелов.

Sample Input:
3

Sample Output:
1 0 0
0 1 0
0 0 1
"""

N = int(input())
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))


def func_1():
    """1-ое решение."""
    t2 = ()
    for i in range(N):
        row = ()
        for j in range(N):
            row += (t[i][j]),
        t2 += (row,)

    [print(*i) for i in t2]


def func_2():
    """2-ое решение."""
    t2 = tuple(t[i][:N] for i in range(N))
    for row in t2:
        print(*row)


def func_3():
    """3-е решение."""
    [print(*row) for row in tuple(t[i][:N] for i in range(N))]


if __name__ == '__main__':
    func_1()
    print()
    func_2()
    print()
    func_3()
