"""
На вход программе подается натуральное число n. Напишите программу, которая
выводит первые n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n(n≥1).

Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, каждую на
отдельной строке, в соответствии с образцом.

Тестовые данные

Sample Input 1:
4

Sample Output 1:
1
1 1
1 2 1
1 3 3 1

Sample Input 2:
5

Sample Output 2:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Sample Input 3:
2

Sample Output 3:
1
1 1
"""


def pascal(n):
    """Выводит первые n строк треугольника Паскаля,
    каждую на отдельной строке.
    """
    pascal_lst = []

    for i in range(n):
        lst = [1] * (i + 1)
        for j in range(1, i):
            lst[j] = pascal_lst[i - 1][j - 1] + pascal_lst[i - 1][j]
        pascal_lst.append(lst)

    for lst in pascal_lst:
        print(*lst)


if __name__ == '__main__':
    n = int(input())
    pascal(n)
