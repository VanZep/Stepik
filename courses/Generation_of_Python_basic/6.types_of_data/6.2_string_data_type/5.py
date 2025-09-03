"""
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
можно ли из длин этих строк построить арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES» (без кавычек), если из длин введённых
слов можно построить арифметическую прогрессию, или «NO» (без кавычек) в
противном случае.

Примечание. Почитать про арифметическую прогрессию можно по ссылке.

Тестовые данные

Sample Input 1:
abc
a
abcde

Sample Output 1:
YES

Sample Input 2:
2434
90099
21

Sample Output 2:
NO

Sample Input 3:
aaaaaaaaaa10
1111111Nm
22222r

Sample Output 3:
YES
"""

str1, str2, str3 = input(), input(), input()

min_length = len(min((str1, str2, str3), key=len))
max_length = len(max((str1, str2, str3), key=len))
mid_length = len(str1 + str2 + str3) - min_length - max_length

if (min_length + max_length) / 2 == mid_length:
    print('YES')
else:
    print('NO')
