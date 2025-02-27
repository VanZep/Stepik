"""
На вход программе подаются два натуральных числа a, b (a < b), записанные
через пробел. Прочитайте их и выполните генерацию целочисленной случайной
величины в диапазоне [a; b]. Выведите результат на экран.

Sample Input:
-2 3

Sample Output:
-1
"""

from random import seed, randint

seed(1)
a, b = map(int, input().split())
print(randint(a, b))
