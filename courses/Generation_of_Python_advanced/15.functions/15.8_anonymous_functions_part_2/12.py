"""
На вход программе на первой строке подаются коэффициенты многочлена,
разделенные символом пробела и целое число x на второй строке. Напишите
программу, которая вычисляет значение указанного многочлена при заданном
значении x.

Формат входных данных
На вход программе на первой строке подаются коэффициенты многочлена
(целые числа), разделенные символом пробела и целое число x на второй строке.

Формат выходных данных
Программа должна вывести одно число — значение указанного многочлена при
заданном значении x.

Примечание 1. Первый тест задает многочлен 2x**2+4x+3, второй тест задает
многочлен x**6+2x**5+3x**4+4x**3+5x*2+6x+7

Примечание 2. Решение задачи необходимо оформить в виде функции
evaluate(coefficients, x), которая принимает список коэффициентов и значение
аргумента. Функция evaluate() должна быть реализована на основе встроенных
функций map() и reduce().

Примечание 3. Не забудьте вызвать функцию evaluate(), чтобы вывести результат.

Тестовые данные

Sample Input 1:
2 4 3
10

Sample Output 1:
243

Sample Input 2:
1 2 3 4 5 6 7
1

Sample Output 2:
28
"""

from functools import reduce


def evaluate(coefficients, x):
    q = list(map(lambda num: x ** num, reversed(range(len(coefficients)))))
    res = reduce(lambda x, y: x + y[0] * y[1], zip(coefficients, q), 0)

    return res


if __name__ == '__main__':
    print(evaluate(list(map(int, input().split())), int(input())))
