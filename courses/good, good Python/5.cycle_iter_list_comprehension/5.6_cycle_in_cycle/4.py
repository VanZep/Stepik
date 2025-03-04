"""
На вход программе подается двумерный список размерностью 5 х 5 элементов,
состоящий из нулей и в некоторых позициях единицы (см. пример ниже).
В программе уже реализовано их чтение и сохранение в списке:
s = sys.stdin.readlines()
lst = [list(map(int, x.strip().split())) for x in s]

Требуется проверить, не касаются ли единицы друг друга по горизонтали,
вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули.
Если проверка проходит вывести на экран "ДА", иначе "НЕТ".

Sample Input:
1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output:
ДА
"""
import sys

s = sys.stdin.readlines()
lst = [list(map(int, x.strip().split())) for x in s]

flag = True

for i in range(len(lst) - 1):
    for j in range(len(lst) - 1):
        if lst[i][j] + lst[i + 1][j] + lst[i][j + 1] + lst[i + 1][j + 1] > 1:
            flag = False

print(['НЕТ', 'ДА'][flag])
