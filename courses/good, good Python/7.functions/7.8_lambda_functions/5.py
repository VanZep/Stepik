"""
В программе задана функция filter_lst:
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res
которая отбирает элементы, переданного ей итерируемого объекта и возвращает
сформированный кортеж значений.

На вход программы поступает список целых чисел, записанных через пробел.
Необходимо прочитать эти числа и сохранить в списке digs. Затем, вызовите
функцию filter_lst несколько раз для формирования:
- кортежа из всех значений списка digs (передается в параметр it)
- кортежа только из отрицательных чисел переданного списка digs
- кортежа только из неотрицательных чисел (то есть, включая и 0) переданного
списка digs
- кортежа из чисел в диапазоне [3; 5] переданного списка digs

Для отбора нужных значений формальному параметру key следует передавать
соответствующие определения анонимной функции. Каждый результат работы функции
следует отображать с новой строки командой:
print(*lst)
где lst - кортеж, возвращенный функцией filter_lst.

Sample Input:
5 4 -3 4 5 -24 -6 9 0

Sample Output:
5 4 -3 4 5 -24 -6 9 0
-3 -24 -6
5 4 4 5 9 0
5 4 4 5
"""


def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


if __name__ == '__main__':
    digs = list(map(int, input().split()))
    lst = filter_lst(digs)
    print(*lst)
    lst = filter_lst(digs, lambda x: x < 0)
    print(*lst)
    lst = filter_lst(digs, lambda x: x >= 0)
    print(*lst)
    lst = filter_lst(digs, lambda x: 2 < x < 6)
    print(*lst)
