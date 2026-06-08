"""
В программе выполняется чтение числовых значений в две переменные следующим
образом:
count, total = map(float, input().split())

Необходимо значение count увеличить на два, а значение total уменьшить на 0.3
"""

count, total = map(float, input().split())

count += 2
total -= 0.3
