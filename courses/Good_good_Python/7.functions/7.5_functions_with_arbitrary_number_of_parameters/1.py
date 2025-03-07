"""
Объявите в программе функцию с именем get_even, которая способна принимать
произвольное количество чисел в качестве аргументов. Например:
get_even(1, 2, 3, -5, 10, 8)

Функция должна возвращать список, составленный только из четных переданных ей
значений.

Sample Input:
45 4 8 11 12 0

Sample Output:
4 8 12 0
"""


def get_even(*nums):
    """Возвращает список из четных переданных ей значений."""
    result_list = [num for num in nums if num % 2 == 0]
    return result_list


if __name__ == '__main__':
    nums_list = list(map(int, input().split()))
    print(*get_even(*nums_list))
