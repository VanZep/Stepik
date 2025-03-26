"""
На вход программе подается натуральное число n. Прочитайте это число и
выведите первое найденное натуральное число (то есть, перебирать числа,
начиная с 1), квадрат которого больше значения n. Программу реализовать
с использованием цикла while.

Sample Input:
10

Sample Output:
4
"""

n = int(input())
count = 1

while count ** 2 <= n:
    count += 1

print(count)
