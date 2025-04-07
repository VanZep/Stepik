"""
На вход программе подается число n. Напишите программу, которая создает и
выводит построчно вложенный список, состоящий из n списков
[[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.

Тестовые данные

Sample Input 1:
4

Sample Output 1:
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]

Sample Input 2:
3

Sample Output 2:
[1]
[1, 2]
[1, 2, 3]

Sample Input 3:
1

Sample Output 3:
[1]
"""

n = int(input())

for i in range(n):
    print(list(range(1, i + 2)))
