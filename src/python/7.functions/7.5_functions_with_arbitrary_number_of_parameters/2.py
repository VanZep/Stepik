"""
Объявите в программе функцию с именем get_biggest_city, которой можно
передавать произвольное количество названий городов (строк) через аргументы.
Например:
get_biggest_city('Город 1', 'Город 2', 'Город 3', 'Город 4')

Данная функция должна возвращать название города (строку) наибольшей длины.
Если таких городов несколько, то первый переданный (из наибольших). Программу
реализовать без использования сортировки.

Sample Input:
Питер Москва Самара Воронеж

Sample Output:
Воронеж
"""


def get_biggest_city(*cities):
    """Возвращает название города (строку) наибольшей длины."""
    biggest_city = ''
    for city in cities:
        biggest_city = city if len(city) > len(biggest_city) else biggest_city
    return biggest_city


if __name__ == '__main__':
    cities_list = input().split()
    print(get_biggest_city(*cities_list))
