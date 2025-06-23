"""
Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь
m/n и выводит ее.

Формат входных данных
На вход программе подаются два натуральных числа, числитель и знаменатель
дроби, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести ответ на задачу.

Тестовые данные

Sample Input 1:
3
6

Sample Output 1:
1/2

Sample Input 2:
12
16

Sample Output 2:
3/4

Sample Input 3:
12
12

Sample Output 3:
1

Sample Input 4:
30
2

Sample Output 4:
15
"""

from fractions import Fraction

print(Fraction(int(input()), int(input())))
