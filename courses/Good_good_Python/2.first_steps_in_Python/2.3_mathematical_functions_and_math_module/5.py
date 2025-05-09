"""
Допишите программу для нахождения числа сочетаний из n по k (значения вводятся
в программе), используя формулу
C = n! / k! * (n−k)!, где n!=1 * 2⋅⋯⋅n. Выведите результат в консоль в виде
целого числа с помощью функции print.

Для вычисления факториалов воспользуйтесь соответствующей функцией из
библиотеки math.

Sample Input:
6 3

Sample Output:
20
"""

import math

n, k = map(int, input().split())
c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(int(c))
