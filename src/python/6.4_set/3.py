"""
На вход программе подается строка, содержащая латинские символы, пробелы и
цифры. Необходимо прочитать эту строку и выделить из нее все неповторяющиеся
цифры (символы от 0 до 9). Выведите на экран все найденные уникальные цифры в
одну строчку через пробел в порядке возрастания их значений. Если цифры
отсутствуют, то вывести строку "НЕТ".

Sample Input:
Python 3.9.11 - best language!

Sample Output:
1 3 9
"""

text = input()


def func_1():
    """1-ое решение."""
    nums = set()
    for char in text:
        if char.isdigit():
            nums.add(int(char))
    if nums:
        print(*sorted(nums))
    else:
        print('НЕТ')


def func_2():
    """2-ое решение."""
    import re

    nums = set(map(int, re.findall(r"\d", text)))
    print(*[sorted(nums), ['НЕТ']][len(nums) == 0])


def func_3():
    """3-е решение."""
    from string import digits

    nums = set(int(char) for char in text if char in digits)
    print(*sorted(nums) if nums else ['НЕТ'])


if __name__ == '__main__':
    func_1()
    print()
    func_2()
    print()
    func_3()
