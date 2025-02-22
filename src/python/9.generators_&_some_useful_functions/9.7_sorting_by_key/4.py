"""
Имеется таблица с данными, представленная в формате:
Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да

В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Данные этого списка необходимо разбить по разделителю ";" и представить в виде
двумерного (вложенного) кортежа в формате:
(
    ('Номер', 'Имя', 'Оценка', 'Зачет'),
    (1, 'Иванов', 3, 'Да'),
    (2, 'Петров', 2, 'Нет'),
    ...
)

При этом все числа должны быть представлены как целые числа. Затем,
отсортировать этот кортеж так, чтобы столбцы шли в порядке:
Имя;Зачет;Оценка;Номер

Реализовать эту операцию с помощью сортировки. Результат должен быть
представлен также в виде двумерного кортежа и присвоен переменной с именем
t_sorted.

Программа ничего не должна выводить на экран, только формировать двумерный
кортеж с переменной t_sorted.

Sample Input:
Номер;Имя;Оценка;Зачет
1;Портос;5;Да
2;Арамис;3;Да
3;Атос;4;Да
4;д'Артаньян;2;Нет
5;Балакирев;1;Нет

Sample Output:
True
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# 1-ое решение
order = (1, 3, 2, 0)
t_sorted = ()
for i, item in enumerate(item.split(';') for item in lst_in):
    if i != 0:
        item[0] = int(item[0])
        item[2] = int(item[2])
    t_sorted += (
        tuple(sorted(item, key=lambda x: order.index(item.index(x)))),
    )
print(t_sorted)

# 2-ое решение
t_sorted = tuple(
    ((b, d, int(c), int(a)) if i != 0 else (b, d, c, a))
    for i, (a, b, c, d) in enumerate(item.split(';') for item in lst_in)
)
print(t_sorted)

# 3-е решение
headers = 'Имя;Зачет;Оценка;Номер'
t = tuple(tuple(
    int(el) if el.isdigit() else el for el in st.split(';')
) for st in lst_in)
t_sorted = tuple(zip(*sorted(zip(*t), key=lambda x: headers.find(x[0]))))
print(t_sorted)
