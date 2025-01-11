"""
На вход программе подаются две строки со списком городов, которые объехал
Сергей в 1-й и 2-й годы своего путешествия по России. Необходимо прочитать эти
наборы строк и сохранить их в отдельных списках (или кортежах). Затем,
требуется определить, включал ли его маршрут во 2-й год все города 1-го года
путешествия? Если это так, то вывести "ДА", иначе "НЕТ".

Sample Input:
Москва Казань Самара Москва
Москва Владимир Новгород Казань Самара Москва

Sample Output:
ДА
"""

cities_list_1 = input().split()
cities_list_2 = input().split()


def func_1():
    """1-ое решение."""
    print('ДА' if set(cities_list_1).issubset(set(cities_list_2)) else 'НЕТ')


def func_2():
    """2-ое решение."""
    print(('НЕТ', 'ДА')[set(cities_list_1) <= set(cities_list_2)])


if __name__ == '__main__':
    func_1()
    print()
    func_2()
