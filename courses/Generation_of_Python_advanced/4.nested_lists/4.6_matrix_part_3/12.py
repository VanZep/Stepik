"""
На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m, заполнив ее "спиралью" в соответствии с
образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m –
количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3
символа на каждый элемент. Для этого используйте строковый метод ljust().
Можно обойтись и без ljust(), система примет и такое решение.

Тестовые данные

Sample Input 1:
4 5

Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8

Sample Input 2:
1 6

Sample Output 2:
1  2  3  4  5  6

Sample Input 3:
3 3

Sample Output 3:
1  2  3
8  9  4
7  6  5
"""

n, m = map(int, input().split())
l = [[0] * m for _ in range(n)]
num = 1
k = 0  # уровень квадрата: 0 - внешний, 1 - вложенный и т.д.
product = n * m + 1  # вынесено в переменную, т.к. n и m меняются в цикле

while num < product:
    for j in range(k, m):  # верхняя сторона
        l[k][j] = num
        num += 1
    for i in range(k + 1, n):  # правая сторона
        l[i][j] = num
        num += 1
    if num == product:  # костыль для случаев с маленькими n, m
        break
    for j in range(m - 2, k - 1, -1):  # нижняя сторона
        l[i][j] = num
        num += 1
    for i in range(n - 2, k, -1):  # левая сторона
        l[i][j] = num
        num += 1
    m -= 1  # изменяю размер сторон для будущего квадрата
    n -= 1
    k += 1

for row in l:
    for el in row:
        print(str(el).ljust(3), end='')
    print()
