"""
Треугольник Паскаля – бесконечная таблица биномиальных коэффициентов, имеющая
треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы.
Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....

На вход программе подается число n. Напишите программу, которая возвращает
указанную строку треугольника Паскаля в виде списка (нумерация строк
начинается с нуля).

Формат входных данных

На вход программе подается натуральное число n(n≥0).

Формат выходных данных

Программа должна вывести указанную строку треугольника Паскаля в виде списка.


Тестовые данные

Sample Input 1:
0

Sample Output 1:
[1]

Sample Input 2:
1

Sample Output 2:
[1, 1]

Sample Input 3:
2

Sample Output 3:
[1, 2, 1]

Sample Input 4:
3

Sample Output 4:
[1, 3, 3, 1]
"""

n = int(input())
last_lst = []

for i in range(n + 1):
    lst = [1] * (i + 1)
    for j in range(1, i):
        lst[j] = last_lst[j - 1] + last_lst[j]
    last_lst = lst

print(lst)
