"""
Комплексные числа хранятся в списке numbers. Дополните приведенный код так,
чтобы он вывел комплексное число с наибольшим модулем и сам модуль числа на
отдельных строках.
"""

numbers = [
    3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j,
    3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
    1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j
]

# print(max(map(abs, numbers)))

max_num = numbers[0]
for num in numbers:
    if abs(max_num) < abs(num):
        max_num = num

print(max_num, abs(max_num), sep='\n')
