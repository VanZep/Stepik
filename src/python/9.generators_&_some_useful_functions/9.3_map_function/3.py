"""
На вход программе подается таблица целых чисел. Строки этой таблицы уже в
программе читаются командой:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Далее, используя функцию map и генератор списков, преобразуйте строки списка
lst_in в двумерный (вложенный) список с именем lst2D, содержащий целые числа
(а не их строковое представление). Сам список lst_in не менять.

Выводить на экран ничего не нужно, только сформировать список lst2D на основе
введенных данных.

Sample Input:
8 11 -5
3 4 10
-1 -2 3
4 5 6

Sample Output:
True
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = list(list(map(int, i.split())) for i in lst_in)
print(lst2D)
