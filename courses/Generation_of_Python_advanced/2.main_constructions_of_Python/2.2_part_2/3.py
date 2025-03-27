"""
На вход программе подается строка текста из неотрицательных чисел. Из
элементов строки формируется список чисел. Напишите программу, которая
меняет местами соседние элементы списка
(a[0] c a[1], a[2] c a[3] и так далее). Если в списке нечетное количество
элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая неотрицательные числа,
разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним
пробелом.

Тестовые данные

Sample Input 1:
1 2 3 4 5

Sample Output 1:
2 1 4 3 5

Sample Input 2:
2 3 2 4

Sample Output 2:
3 2 4 2

Sample Input 3:
1

Sample Output 3:
1
"""


def func_1():
    """1-ое решение."""
    nums = input().split()
    for i in range(0, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(*nums)


def func_2():
    """2-ое решение."""
    nums = input().split()
    nums[:-1:2], nums[1::2] = nums[1::2], nums[:-1:2]
    print(*nums)


if __name__ == '__main__':
    func_1()
    func_2()
