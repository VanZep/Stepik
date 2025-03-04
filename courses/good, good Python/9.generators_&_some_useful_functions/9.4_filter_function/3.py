"""
На вход программе подаются целые числа, записанные через пробел. Необходимо их
прочитать и оставить среди них только двузначные числа. Реализовать программу с
использованием функции filter. Результат отобразить на экране в виде
последовательности оставшихся чисел в одну строчку через пробел.

Sample Input:
8 11 0 -23 140 1

Sample Output:
11 -23
"""

# 1-й варинт
nums_str = input()
filtered_nums = filter(lambda num: len(num.lstrip('-')) == 2, nums_str.split())
print(*filtered_nums)

# 2-ой варинт
nums_str = map(int, input().split())
filtered_nums = filter(lambda num: 9 < abs(num) < 100, nums_str)
print(*filtered_nums)
