"""
На вход программе подаются строки в формате:
<день рождения 1> имя_1
<день рождения 2> имя_2
...
<день рождения N> имя_N

Дни рождений и имена могут повторяться.

В программе уже реализовано их считывание и сохранение в списке:
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    '3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана'
]

На основе списка lst_in сформировать словарь, где ключи - дни рождения
(целое число), а значения - имена (строка). Выведите полученный словарь
в формате (см. пример ниже):
день рождения 1: имя1, ..., имяN1
день рождения 2: имя1, ..., имяN2
...
день рождения M: имя1, ..., имяNM

Sample Input:
3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана

Sample Output:
3: Сергей
5: Николай, Юлия
4: Елена, Светлана
7: Владимир
"""

lst_in = [
    '3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана'
]


def func():
    """Решение."""
    d = {}
    for i in lst_in:
        num, name = i.split()
        if d.get(num):
            d[num] += f', {name}'
        else:
            d[num] = name

    for key, value in d.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    func()
