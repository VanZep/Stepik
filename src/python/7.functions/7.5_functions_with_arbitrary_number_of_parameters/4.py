"""
На вход программе подается таблица целых чисел (см. пример ниже)
размером N x N элементов (N определяется по входным данным). Необходимо
прочитать эти числа и сохранить в виде двумерного (вложенного) списка lst2D
размером N x N элементов. Полученная таблица будет содержать нули и кое-где
единицы. С помощью функции с именем verify, на вход которой подается
двумерный список чисел (первый параметр), необходимо проверить, являются ли
единицы изолированными друг от друга, то есть, вокруг каждой единицы должны
быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор
двумерного списка. Для каждого элемента (списка) со значением 1 вызывать еще
одну вспомогательную функцию is_isolate для проверки изолированности единицы.
То есть, функция is_isolate должна возвращать True, если единица изолирована
и False в противном случае.

Как только встречается не изолированная единица, функция verify должна
возвращать False. Если успешно доходим (по элементам списка) до конца,
то возвращается значение True.

Sample Input:
1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

1 0 0 0 0
0 0 1 0 0
0 0 1 0 0
0 1 0 1 0
0 0 0 0 0

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
1 1 1 1 1

Sample Output:
True
"""

import sys
import copy

lines = sys.stdin.readlines()
lst2D = [list(map(int, i.strip().split())) for i in lines]


def verify_1(lst):
    """1-ое решение."""
    for i in range(len(lst) - 1):
        for j in range(len(lst[0]) - 1):
            if lst[i][j] + lst[i + 1][j] + lst[i][j + 1] + lst[i + 1][
                j + 1] > 1:
                return False
    return True


def expand_list(lst_in):
    lst = copy.deepcopy(lst_in)
    lst.append(N * [0])
    lst.insert(0, N * [0])
    for row in lst:
        row.insert(0, 0)
        row.append(0)
    return lst


def is_isolate(i, j):
    return sum(
        expanded_lst2D[i][j:j + 2]
        + expanded_lst2D[i + 1][j:j + 2]
        + expanded_lst2D[i + 2][j:j + 2]
    ) == 1


def verify_2(lst):
    """2-ое решение."""
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                if not is_isolate(i, j):
                    return False
    return True


if __name__ == '__main__':
    N = len(lst2D)
    print(verify_1(lst2D))
    expanded_lst2D = expand_list(lst2D)
    print(verify_2(lst2D))
