"""
На вход программе подается матрица чисел из трех строк. В каждой строке числа
разделяются пробелом. Необходимо прочитать эти числа и сохранить в виде
двумерного (вложенного) списка. Затем, вывести на экран последний столбец
этой матрицы (двумерного списка) в виде строки из трех чисел, записанных
через пробел.

Sample Input:
8 11 12 1
9 4 36 -4
1 12 49 5

Sample Output:
1 -4 5
"""

x = [
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split()))
]
print(x[0][-1], x[1][-1], x[2][-1])
