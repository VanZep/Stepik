"""
На вход программе подается строка со словами, записанными через пробел.
Необходимо прочитать эту строку и с помощью генераторов множеств и словарей
сформировать словарь в формате:
{слово_1: количество_1, слово_2: количество_2, ..., слово_N: количество_N}

То есть, ключами выступают уникальные слова (без учета регистра),
а значениями - число их встречаемости в тексте. На экран вывести значение
словаря для слова (союза) 'и'. Если такого ключа нет, то вывести 0.

Sample Input:
И что сказать и что сказать и нечего и точка

Sample Output:
4
"""

words_lst = input().lower().split()


def func_1():
    """1-ое решение."""
    words_set = {word for word in words_lst}
    words_dict = {key: words_lst.count(key) for key in words_set}
    print(words_dict.get('и', 0))


def func_2():
    """2-ое решение."""
    words_dict = {
        key: words_lst.count(key) for key in {word for word in words_lst}
    }
    print(words_dict.get('и', 0))


def func_3():
    """3-е решение."""
    words_dict = {word: words_lst.count(word) for word in words_lst}
    print(words_dict.get('и', 0))


if __name__ == '__main__':
    func_1()
    print()
    func_2()
    print()
    func_3()
