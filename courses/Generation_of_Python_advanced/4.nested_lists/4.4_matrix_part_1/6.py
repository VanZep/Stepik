"""
Напишите программу, которая выводит максимальный элемент в заштрихованной
области квадратной матрицы > img_2.png.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в
матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число – максимальный элемент в заштрихованной
области квадратной матрицы.

Примечание. Элементы диагоналей также учитываются.

Тестовые данные

Sample Input 1:
3
1 4 5
6 7 8
1 1 6

Sample Output 1:
8

Sample Input 2:
4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0

Sample Output 2:
7

Sample Input 3:
2
6 0
7 9

Sample Output 3:
9
"""

from sys import maxsize

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_num = -maxsize - 1

for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j or i <= j and i >= n - 1 - j:
            max_num = max(max_num, matrix[i][j])

print(max_num)
