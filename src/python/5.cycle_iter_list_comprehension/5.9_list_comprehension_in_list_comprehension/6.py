"""
Нужно транспонировать список lst_in (строки заменяются на столбцы) и результат
сохранить в списке A. Отобразите полученный список A с помощью следующей
конструкции:

for row in A:
    print(*row)

Sample Input:
1 2 3
4 5 6
7 8 9
5 4 3
"""

lst_in = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [5, 4, 3]
]

A = [
    [lst_in[row][i] for row in range(len(lst_in))]
    for i in range(len(lst_in[0]))
]

for row in A:
    print(*row)
