"""
Даны по 10-балльной шкале оценки по информатике трех учеников. Напишите
программу, выводящую множество оценок, которые есть и у первого, и у второго
учеников, но которых нет у третьего ученика.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела
(оценки каждого ученика на отдельной строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке,
разделенных пробелами, в соответствии с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

Тестовые данные

Sample Input 1:
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10

Sample Output 1:
5 3 2

Sample Input 2:
2 9 3 4 6 10
2 3 4 5 2 10
2 3 4 5 3 9

Sample Output 2:
10

Sample Input 3:
3 4 5 6 2 10 3 9 8 8
5 7 8 9 2 7 4 6 8 2
2 6 7 1 3 6 5 9 2 6

Sample Output 3:
8 4
"""

print(*sorted(
    set(
        input().split()
    ).intersection(
        input().split()
    ).difference(
        input().split()
    ),
    key=int, reverse=True
))
