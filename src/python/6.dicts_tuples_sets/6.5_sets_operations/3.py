"""
На вход программе подаются два списка целых чисел, каждый с новой строки
(в строке наборы чисел следующих через пробел). Необходимо прочитать эти
наборы чисел и сохранить их в отдельных списках (или кортежах). Затем,
с помощью множеств(а) выбрать уникальные числа, присутствующие в первом или
втором списках, но отсутствующие одновременно в обоих. Результат выведите на
экран в виде строки чисел, записанных по возрастанию через пробел, используя
команду (здесь s - это множество, содержащее уникальные числа):
print(*sorted(s))

Sample Input:
1 2 3 4 5
4 5 6 7 8

Sample Output:
1 2 3 6 7 8
"""

tup_1 = tuple(map(int, input().split()))
tup_2 = tuple(map(int, input().split()))


def func_1():
    """1-ое решение."""
    s = set(tup_1) ^ set(tup_2)
    print(*sorted(s))


def func_2():
    """2-ое решение."""
    s = set(tup_1).symmetric_difference(set(tup_2))
    print(*sorted(s))


if __name__ == '__main__':
    func_1()
    print()
    func_2()