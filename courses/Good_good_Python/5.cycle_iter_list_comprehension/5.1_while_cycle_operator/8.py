"""
На вход программе подается целое положительное число n (количество часов).
Прочитайте это число и сохраните в переменной n.

Пусть одноклеточная амеба каждые 3 часа делится на 2 клетки. Необходимо
определить, сколько клеток будет через n часов. Считать, что изначально
была одна амеба.

Результат (итоговое число клеток) вывести на экран. Задачу необходимо решить с
использованием цикла while.

Sample Input:
11

Sample Output:
8
"""

n = int(input())
x = 1
while n > 3:
    x *= 2
    n -= 3

print(x)
