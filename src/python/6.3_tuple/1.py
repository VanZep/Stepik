"""
Объявите в программе следующий кортеж:
t = (3.4, -56.7)
На вход программе подается последовательность целых чисел, записанных через
пробел. Необходимо их прочитать и добавить в конец кортежа t. Добавленные числа
в кортеже должны следовать в порядке их считывания. Результат вывести на экран
командой:
print(t)

Sample Input:
8 11 -5 2

Sample Output:
(3.4, -56.7, 8, 11, -5, 2)
"""


def func():
    """Решение."""
    t = (3.4, -56.7) + tuple(map(int, input().split()))
    print(t)


if __name__ == '__main__':
    func()
