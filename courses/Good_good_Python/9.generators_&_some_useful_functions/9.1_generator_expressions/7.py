"""
Необходимо объявить генератор, который бы выдавал значения функции:
f(x) = 1/2⋅x**2−2
для аргумента x в диапазоне [a; b] (включительно) с шагом 0.01.
Целые числа a, b (a < b) подаются на вход программе в одну строчку через
пробел. Нужно их прочитать и через генератор вывести на экран первые 20
значений функции с точностью до сотых.

P.S. Значения функции в генераторе вычислять командой:
f(x) = 0.5 * pow(x, 2) - 2.0

Sample Input:
0 10
-2 2

Sample Output:
-2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -1.99 -1.99 -1.99 -1.99
-1.99 -1.99 -1.99 -1.98 -1.98
0.0 -0.02 -0.04 -0.06 -0.08 -0.1 -0.12 -0.14 -0.16 -0.18 -0.2 -0.21 -0.23
-0.25 -0.27 -0.29 -0.31 -0.33 -0.34 -0.36
"""

STEP = 100
a, b = map(int, input().split())
fx = lambda x: 0.5 * pow(x / STEP, 2) - 2.0
gen = (round(fx(x), 2) for x in range(a * STEP, b * STEP + 1))
print(*(next(gen) for _ in range(20)))
