"""
На вход программе подается натуральное число n. Прочитайте это число и с
помощью цикла for определите является ли оно простым (то есть, делится
нацело только на само себя и на 1). Вывести на экран строку "ДА", если n
простое и строку "НЕТ" в противном случае.

Sample Input:
11

Sample Output:
ДА
"""

n = int(input())
count = 0

for x in range(1, n + 1):
    if n % x == 0:
        count += 1

if count == 2:
    print('ДА')
else:
    print('НЕТ')
