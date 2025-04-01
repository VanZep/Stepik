"""
На вход программе подается натуральное число n. Прочитайте это число и с
помощью цикла for найдите все делители этого числа (то есть, целые числа
от 1 до n, которые делят число n нацело). Найденные делители выводить
сразу в столбик без формирования списка.

Sample Input:
12

Sample Output:
1
2
3
4
6
12
"""

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
