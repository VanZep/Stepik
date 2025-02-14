"""
На вход программе подается натуральное число n. Необходимо его прочитать и
найти все простые числа (нацело делятся только на 1 и на себя), которые меньше
числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку
через пробел.

Ликбез: квадратная скобка - граница включается; круглая скобка - граница
исключается. Например [2; n) - диапазон от 2 до n-1 целых чисел.

Sample Input:
11

Sample Output:
2 3 5 7
"""


def func_1():
    """1-ое решение."""
    n = int(input())
    lst = [i for i in range(2, n)]
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                print(i, '- составное число')
                lst.remove(i)
                break

    print(*lst)


def func_2():
    """2-ое решение."""
    n = int(input())
    for i in range(2, n):
        for j in range(2, i):
            if not i % j:
                break
        else:
            print(i, end=' ')


if __name__ == '__main__':
    func_1()
    print()
    func_2()
