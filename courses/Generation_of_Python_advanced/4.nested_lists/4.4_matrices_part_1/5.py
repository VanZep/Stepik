"""
Напишите программу, которая выводит максимальный элемент в заштрихованной
области квадратной матрицы.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в
матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число – максимальный элемент в заштрихованной
области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.

Тестовые данные

Sample Input 1:
3
1 4 5
6 7 8
1 1 6

Sample Output 1:
7

Sample Input 2:
4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0

Sample Output 2:
0

Sample Input 3:
2
6 0
7 9

Sample Output 3:
9

Sample Input 4:
3
-50 -10 -20
-19 -78 -70
-11 -12 -19

Sample Output 4:
-11
"""

from sys import maxsize

# 1-ое решение
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_num = -maxsize - 1

for i in range(n):
    for j in range(i + 1):
        max_num = max(max_num, matrix[i][j])

print(max_num)

# 2-ое решение
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_num = -maxsize - 1

for i in range(n):
    for j in range(n):
        if i >= j:
            max_num = max(max_num, matrix[i][j])

print(max_num)
