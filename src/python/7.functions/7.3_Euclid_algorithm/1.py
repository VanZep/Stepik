"""
Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя
двух натуральных чисел a и b. В программе необходимо объявить функцию get_nod с
двумя параметрами a и b (натуральные числа) и возвращающую значение НОД(a, b).

Sample Input:
15 121050

Sample Output:
15
"""

x, y = map(int, input().split())


def get_node(a, b):
    """Вычисляет наибольший общий делитель для двух чисел
    по быстрому алгоритму Евклида.
    """
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(get_node(x, y))
