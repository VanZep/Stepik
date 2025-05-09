"""
На вход программе подается строка. Требуется ее прочитать и сформировать N=10
пар кортежей в формате:
(символ, порядковый индекс)

Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может
быть и длиннее. То есть, число пар может быть 10 и менее. Используя функцию zip
сформируйте указанные кортежи и сохраните их списке с именем lst.

P.S. Программа ничего не должна отображать на экране, только формировать
список lst из кортежей.

Sample Input:
Sergey Balakirev

Sample Output:
[
    ('S', 0), ('e', 1), ('r', 2), ('g', 3), ('e', 4),
    ('y', 5), (' ', 6), ('B', 7), ('a', 8), ('l', 9)
]
"""

N = 10
string = input()
lst = [*zip(string, range(N))]
print(lst)
