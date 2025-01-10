"""
В аккаунте YouTube Сергея прокомментировали очередное видео. Некоторые
посетители оставляли несколько комментариев. Требуется по списку комментариев
определить уникальное число комментаторов (полагается, что имена у разных
комментаторов не совпадают). Комментарии поступают на вход программе в формате:
имя 1: комментарий 1
имя 2: комментарий 2
...
имя N: комментарий N

В программе уже реализовано считывание этих строк и сохранение в списке:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Выведите на экран общее число уникальных комментаторов.

Sample Input:
EvgeniyK: спасибо большое!
LinaTroshka: лайк и подписка!
Sergey Karandeev: крутое видео!
Евгений Соснин: обожаю
EvgeniyK: это повтор?
Sergey Karandeev: нет, это новое видео

Sample Output:
4
"""

from sys import stdin

lst_in = list(map(str.strip, stdin.readlines()))


def func_1():
    """1-ое решение."""
    unique_names = set()
    for comment in lst_in:
        unique_names.add(comment.split(':')[0])
    print(len(unique_names))


def func_2():
    """2-ое решение."""
    print(len(set(comment.split(':')[0] for comment in lst_in)))


if __name__ == '__main__':
    func_1()
    print()
    func_2()
