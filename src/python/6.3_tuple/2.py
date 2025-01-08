"""
На вход программе подается строка с названиями городов, записанных через
пробел. Необходимо прочитать эту строку и на ее основе сформировать кортеж из
названий городов. Названия в кортеже должны идти в том же порядке, что и в
исходной строке. Выполните проверку: если в полученном кортеже нет города
"Москва", то следует его добавить в конец кортежа. Выведите на экран названия
городов из кортежа (по порядку) в одну строчку через пробел.

Sample Input:
Уфа Казань Самара

Sample Output:
Уфа Казань Самара Москва
"""

cities_tuple = tuple(input().split())
MOSCOW = 'Москва'


def func(cities):
    """Решение."""
    cities = cities + (MOSCOW,) if MOSCOW not in cities else cities
    print(*cities)


if __name__ == '__main__':
    func(cities_tuple)
