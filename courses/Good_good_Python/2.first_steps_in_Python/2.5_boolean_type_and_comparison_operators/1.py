"""
Напишите программу, которая из входного потока читает вещественное число.
Нужно определить, что целая часть прочитанного числа кратна 3. На экран
вывести True, если кратно и False - в противном случае. Задача делается без
использования условного оператора.

Sample Input:
78.34

Sample Output:
True
"""

from math import floor

a = float(input())
print((floor(a) % 3) == 0)
