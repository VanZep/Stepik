"""
На вход программе подается таблица целых чисел, записанных через пробел.
В программе уже реализовано чтение ее строк:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Необходимо преобразовать список строк lst_in в двумерный список чисел. Затем,
в полученном списке (таблице) перемешать столбцы, используя функции shuffle и
zip. Результат вывести на экран (также в виде таблицы). При выводе в конце
строк не должно быть пробелов.

Sample Input:
1 2 3 4
5 6 7 8
9 8 6 7

Sample Output:
4 1 3 2
8 5 7 6
7 9 6 8
"""

import sys
from random import seed, shuffle

seed(1)
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2d = list(zip(*[list(map(int, item.split())) for item in lst_in]))
shuffle(lst2d)
for row in zip(*lst2d):
    print(*row)
