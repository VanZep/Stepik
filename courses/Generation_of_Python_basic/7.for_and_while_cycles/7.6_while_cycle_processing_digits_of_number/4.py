"""
Дано натуральное число. Напишите программу, которая вычисляет:
- сумму его цифр
- количество цифр в нем
- произведение его цифр
- среднее арифметическое его цифр
- его первую цифру
- сумму его первой и последней цифры

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке, каждое на отдельной строке.

Тестовые данные

Sample Input 1:
5678

Sample Output 1:
26
4
1680
6.5
5
13

Sample Input 2:
132

Sample Output 2:
6
3
6
2.0
1
3

Sample Input 3:
75

Sample Output 3:
12
2
35
6.0
7
12
"""
from itertools import product

"""
- сумму его цифр
- количество цифр в нем
- произведение его цифр
- среднее арифметическое его цифр
- его первую цифру
- сумму его первой и последней цифры
"""

n = num = int(input())
sum_digits = 0
count_digits = 0
product_digits = 1

while num != 0:
    last_digit = num % 10
    sum_digits += last_digit
    num //= 10

    count_digits += 1

    product_digits *= last_digit

first_digit = n // 10 ** (count_digits - 1)
sum_first_last_digit = first_digit + n % 10

print(
    sum_digits,
    count_digits,
    product_digits,
    sum_digits / count_digits,
    first_digit,
    sum_first_last_digit,
    sep='\n'
)
