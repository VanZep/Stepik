"""
На вход программе подается натуральное число N. Прочитайте его и с помощью
list comprehension сформируйте двумерный список размером N x N, состоящий из
нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы,
идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого
угла). Полученный двумерный список отобразите в виде таблицы чисел, как
показано в примере ниже.

Sample Input:
4

Sample Output:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
"""

n = int(input())
matrix = [['1' if i == j else '0' for i in range(n)] for j in range(n)]

for row in matrix:
    print(*row)
