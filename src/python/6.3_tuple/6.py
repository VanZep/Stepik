"""
На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в кортеже. Затем, в кортеже найти и
вывести в одну строчку через пробел (по порядку) все индексы неуникальных
(повторяющихся) значений.

Sample Input:
5 4 -3 2 4 5 10 11

Sample Output:
0 1 4 5
"""

nums = tuple(input().split())


def func_1():
    """1-ое решение."""
    for i, num in enumerate(nums):
        if nums.count(num) > 1:
            print(i, end=' ')
    print()


def func_2():
    """2-ое решение."""
    indexes = ()
    for i, num in enumerate(nums):
        if nums.count(num) > 1:
            indexes += (i,)

    print(*indexes)


if __name__ == '__main__':
    func_1()
    print()
    func_2()
