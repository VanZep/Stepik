"""
На вход программе подается двумерный список размерностью 5 х 5 элементов,
состоящий из целых чисел (пример см. ниже). В программе уже реализовано их
чтение и сохранение в списке:
s = sys.stdin.readlines()
lst = [list(map(int, x.strip().split())) for x in s]

Необходимо проверить, является ли этот двумерный список симметричным
относительно главной диагонали. Главная диагональ — та, которая идёт из левого
верхнего угла двумерного массива в правый нижний. Выведите на экран "ДА",
если матрица (таблица чисел) симметрична и "НЕТ" в противном случае.

Sample Input:
2 3 4 5 6
3 2 7 8 9
4 7 2 0 4
5 8 0 2 1
6 9 4 1 2

Sample Output:
ДА
"""
import sys

s = sys.stdin.readlines()
lst = [list(map(int, x.strip().split())) for x in s]
flag = True

for i in range(len(lst)):
    if not flag:
        break
    for j in range(len(lst)):
        if lst[i][j] != lst[j][i]:
            flag = False
            break

print(['НЕТ', 'ДА'][flag])
