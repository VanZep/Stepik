"""
На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в кортеже. Затем, создать еще один кортеж
с уникальными (не повторяющимися) значениями из первого кортежа. Уникальные
числа должны следовать в том же порядке, что и в исходном кортеже. Отобразите
найденные уникальные числа в одну строчку через пробел.

P.S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве
практики пока обойдемся без них.

Sample Input:
8 11 -5 -2 8 11 -5

Sample Output:
8 11 -5 -2
"""

nums = tuple(input().split())


def func_1():
    """1-ое решение."""
    lst = []
    [lst.append(num) for num in nums if num not in lst]
    unique_nums = tuple(lst)
    print(*unique_nums)


def func_2():
    """2-ое решение."""
    unique_nums = ()
    for num in nums:
        if num not in unique_nums:
            unique_nums += (num,)
    print(*unique_nums)


def func_3():
    """3-е решение."""
    unique_nums = tuple(dict.fromkeys(nums))
    print(*unique_nums)


if __name__ == '__main__':
    func_1()
    print()
    func_2()
    print()
    func_3()
