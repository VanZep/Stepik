"""
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в
матрице, затем элементы матрицы, затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом
пробела.

Тестовые данные

Sample Input 1:
3
1 2 3
4 5 6
7 8 9
2

Sample Output 1:
30 36 42
66 81 96
102 126 150

Sample Input 2:
3
1 2 1
3 3 3
1 2 1
5

Sample Output 2:
1666 2222 1666
3333 4443 3333
1666 2222 1666

Sample Input 3:
5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3

Sample Output 3:
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
"""

from copy import deepcopy

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
current_matrix = matrix

for m in range(m - 1):
    result_matrix = [[0] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result_matrix[k][i] += matrix[j][i] * current_matrix[k][j]
    current_matrix = deepcopy(result_matrix)

for row in result_matrix:
    print(*row)
