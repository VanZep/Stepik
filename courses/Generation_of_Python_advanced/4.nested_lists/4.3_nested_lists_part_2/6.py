"""
На вход программе подаются две строки: на одной – символы, на другой – число n.
Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков (кусков)
указанной длины.

Формат входных данных
На вход программе подаются строка текста, содержащая символы, разделенные
символом пробела, и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Тестовые данные

Sample Input 1:
a b c d e f
2

Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]

Sample Input 2:
a b c d e f
3

Sample Output 2:
[['a', 'b', 'c'], ['d', 'e', 'f']]

Sample Input 3:
a b c d e f
6

Sample Output 3:
[['a', 'b', 'c', 'd', 'e', 'f']]

Sample Input 4:
a b c d e f r g b
2

Sample Output 4:
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]

Sample Input 5:
a b
3

Sample Output 5:
[['a', 'b']]
"""


def chunked(lst, chunk):
    return [lst[i: i + chunk] for i in range(0, len(lst), chunk)]


if __name__ == '__main__':
    chars = input().split()
    n = int(input())
    print(chunked(chars, n))
