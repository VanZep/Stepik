"""
На вход программе подаются вещественные числа, записанные через пробел.
Необходимо их прочитать и определить, есть ли среди них хотя бы одно
отрицательное. Вывести True, если это так и False в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
8.2 -11.0 20 3.4 -1.2

Sample Output:
True
"""

float_nums = tuple(map(float, input().split()))
print(any(map(lambda x: x < 0, float_nums)))
print(any(x < 0 for x in float_nums))
