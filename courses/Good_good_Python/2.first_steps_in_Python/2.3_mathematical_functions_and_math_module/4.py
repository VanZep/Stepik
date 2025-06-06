"""
Допишите текст программы для вычисления евклидового расстояния (гипотенузы)
по перемещениям a и b (формула:(a**2+b**2)**0.5). Округлите результат с
точностью до сотых. Полученное значение выведите на экран.

Sample Input:
3 4

Sample Output:
5.0
"""

import math

a, b = map(int, input().split())
print(round(math.sqrt(a ** 2 + b ** 2), 2))
print(round((a ** 2 + b ** 2) ** 0.5, 2))
