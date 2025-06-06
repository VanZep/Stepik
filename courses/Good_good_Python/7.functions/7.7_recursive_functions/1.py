"""
На вход программе подается целое положительное число N. Необходимо написать
рекурсивную функцию с именем get_rec_N, которая отображает на экране
последовательность целых чисел от 1 до N (включительно). Каждое число
выводится с новой строки.

В качестве единственного параметра функция get_rec_N должна принимать числовое
значение. Начальный вызов функции уже дан в программе и выглядит так:
get_rec_N(N)

Sample Input:
8

Sample Output:
1
2
3
4
5
6
7
8
"""


def get_rec_N(num, min_num=1):
    """Выводит в консоль последовательность целых чисел
    от 1 до N (включительно).
    """
    if num > min_num:
        get_rec_N(num - 1)
    print(num)


if __name__ == '__main__':
    N = int(input())
    get_rec_N(N)
