"""
Дополните приведенный код так, чтобы он вывел сумму наибольшей и наименьшей
цифры Decimal числа.

Тестовые данные

Sample Input 1:
12.1244354689

Sample Output 1:
10

Sample Input 2:
0.1244354689

Sample Output 2:
9
"""

from decimal import Decimal

num = Decimal(input())

if int(num) == 0:
    print(max(num.as_tuple().digits))
else:
    num_digits = num.as_tuple().digits
    print(min(num_digits) + max(num_digits))
