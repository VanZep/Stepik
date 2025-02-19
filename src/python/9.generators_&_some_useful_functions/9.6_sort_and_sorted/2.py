"""
Объявите в программе функцию со следующей сигнатурой:

def get_sort(d): ...
На входе этой функции (в параметре d) ожидается словарь формата (пример):
d = {
    'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево',
    'dog': 'собака', 'book': 'книга'
}

Функция должна выполнить сортировку ключей словаря d по убыванию
(лексикографическая сортировка строк) и возвратить список из соответствующих
значений ключей словаря. Сам словарь d при этом должен оставаться неизменным.
Например, для указанного словаря d, результатом работы функции должен быть
список:
['дерево', 'лошадь', 'собака', 'кот', 'книга']

В программе нужно реализовать только функцию get_sort, вызывать ее не нужно и
что-либо выводить на экран.
"""


def get_sort_1(d):
    """Выполняет сортировку ключей словаря d по убыванию
    и возвращает список из соответствующих значений ключей словаря.
    1-ое решение.
    """
    return [*dict(sorted(d.items(), reverse=True)).values()]


def get_sort_2(d):
    """Выполняет сортировку ключей словаря d по убыванию
    и возвращает список из соответствующих значений ключей словаря.
    2-ое решение.
    """
    return [d[key] for key in sorted(d, reverse=True)]


if __name__ == '__main__':
    dictionary = {
        'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево',
        'dog': 'собака', 'book': 'книга'
    }
    print(get_sort_1(dictionary))
    print(get_sort_2(dictionary))
