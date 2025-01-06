"""
На вход программе подаются данные в формате ключ=значение, записанные через
пробел. Необходимо прочитать строку с этими данными и на их основе сформировать
словарь. Затем проверить, существуют ли в словаре ключи со значениями:
'house', 'True' и '5' (все ключи - строки). Если все они существуют,
то вывести на экран "ДА", иначе "НЕТ".

Sample Input:
вологда=город house=дом True=1 5=отлично 9=божественно

Sample Output:
ДА
"""


def func_1():
    """1-ое решение."""
    d = dict([i.split('=') for i in input().split()])
    lst = ['house', 'True', '5']
    flag = True
    for i in lst:
        if i not in d:
            flag = False
    print(['НЕТ', 'ДА'][flag])


def func_2():
    """2-ое решение."""
    d = dict(i.split('=') for i in input().split())
    print(('НЕТ', 'ДА')[all(i in d for i in ('house', 'True', '5'))])


if __name__ == '__main__':
    func_1()
    func_2()
