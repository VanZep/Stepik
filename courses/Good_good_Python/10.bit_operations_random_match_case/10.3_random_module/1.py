"""
На вход программе подаются два натуральных числа a, b (a < b), записанных
через пробел. Прочитайте их и выполните генерацию вещественной случайной
величины в диапазоне [a; b). Округлите результат до сотых и выведите его
на экран.

Sample Input:
-4 5

Sample Output:
-2.79
"""

from random import seed, uniform

seed(1)
a, b = map(int, input().split())
print(round(uniform(a, b), 2))
