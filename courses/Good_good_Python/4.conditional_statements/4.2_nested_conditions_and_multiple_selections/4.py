"""
На вход программе подается целое число: порядковый номер дня недели
(1, 2, ..., 7). Необходимо прочитать это число и вывести на экран название
дня недели:

понедельник, вторник, среда, четверг, пятница, суббота, воскресенье

Программу реализовать с использованием операторов if-elif.

Sample Input:
2

Sample Output:
вторник
"""

d = int(input())
if d == 1:
    print("понедельник")
elif d == 2:
    print("вторник")
elif d == 3:
    print("среда")
elif d == 4:
    print("четверг")
elif d == 5:
    print("пятница")
elif d == 6:
    print("суббота")
elif d == 7:
    print("воскресенье")
