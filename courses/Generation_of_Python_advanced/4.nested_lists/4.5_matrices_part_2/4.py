"""
Напишите программу, которая проверяет симметричность квадратной матрицы
относительно главной диагонали.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в
матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной
диагонали, или NO в противном случае.

Тестовые данные

Sample Input 1:
3
0 1 2
1 2 3
2 3 4

Sample Output 1:
YES

Sample Input 2:
3
0 1 2
1 2 7
2 3 4

Sample Output 2:
NO

Sample Input 3:
2
1 2
3 4

Sample Output 3:
NO
"""

n = int(input())
matrix = [input().split() for _ in range(n)]
is_symmetric = True


for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

print(['NO', 'YES'][is_symmetric])
