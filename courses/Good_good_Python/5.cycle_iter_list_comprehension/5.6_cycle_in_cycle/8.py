"""
В некоторой стране используются денежные купюры достоинством в
1, 2, 4, 8, 16, 32 и 64. На вход программы подается натуральное число n.
Необходимо его прочитать. Затем определите, каким наименьшим количеством
денежных купюр достоинством в 1, 2, 4, 8, 16, 32 и 64 можно выплатить сумму n?
выведите на экран список купюр для формирования суммы n (в одну строчку через
пробел, начиная с наибольшей и заканчивая наименьшей). Предполагается, что
имеется достаточно большое количество купюр всех достоинств.

P.S. Программа может быть реализована и без вложенных циклов.

Sample Input:
221

Sample Output:
64 64 64 16 8 4 1
"""

n = int(input())
divider_list = [64, 32, 16, 8, 4, 2, 1]
result_list = []

for divider in divider_list:
    multiplier = n // divider
    if multiplier:
        result_list += [divider] * multiplier
        n -= divider * multiplier

print(*result_list)
