"""
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m – количество строк и
столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка.
Далее следуют числа m и k – количество строк и столбцов второй матрицы затем
элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом
пробела.

Тестовые данные

Sample Input 1:
2 2
1 2
3 2

2 2
3 2
1 1

Sample Output 1:
5 4
11 8

Sample Input 2:
3 2
2 5
6 7
1 8

2 3
1 2 1
0 1 0

Sample Output 2:
2 9 2
6 19 6
1 10 1

Sample Input 3:
3 3
2 4 6
1 3 5
0 4 8

3 3
6 3 1
9 6 3
0 2 0

Sample Output 3:
48 42 14
33 31 10
36 40 12
"""

n, m = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(n)]
input()
m, k = map(int, input().split())
matrix_2 = [list(map(int, input().split())) for _ in range(m)]
result_matrix = [[0] * k for _ in range(n)]

for k in range(k):
    for i in range(n):
        for j in range(m):
            result_matrix[k][i] += matrix_1[k][j] * matrix_2[j][i]

for row in result_matrix:
    print(*row)
