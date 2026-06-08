"""
В программе выполняется чтение трех числовых значений следующим образом:
a, b, c = map(float, input().split())

Необходимо вычислить длину по формуле:
L=a**2+b**2+c**2

Результат сохраните в переменной length. Результат округлите до сотых с
помощью функции round().
"""

import math

a, b, c = map(float, input().split())

length = round(
    math.sqrt(math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2)),
    2
)
