"""
Объявите в программе словарь с наименованиями предметов и их весом (в граммах):

things = {
    'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
    'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
    'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130,
    'спички': 10
}
Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный
вес в N кг (вводится с клавиатуры). Он решил класть в рюкзак предметы в
порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так,
чтобы их суммарный вес не превысил значения N кг. Все предметы даны в
единственном экземпляре. Выведите список предметов (в строчку через пробел),
которые берет с собой Сергей в порядке убывания их веса.

Sample Input:
10

Sample Output:
палатка брезент удочка брюки пила карандаш спички
"""

things = {
    'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
    'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
    'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130,
    'спички': 10
}
max_weight = int(input()) * 1000


def func_1(capacity):
    """1-ое решение."""
    fliped_things = {v: k for k, v in things.items()}
    backpack = []

    while fliped_things:
        max_thing_weight = max(fliped_things)
        if capacity >= max_thing_weight:
            capacity -= max_thing_weight
            backpack.append(fliped_things[max_thing_weight])
        del fliped_things[max_thing_weight]

    print(*backpack)


def func_2(capacity):
    """2-ое решение."""
    fliped_things = {v: k for k, v in things.items()}
    backpack = []

    for thing_weight in sorted(fliped_things, reverse=True):
        if capacity >= thing_weight:
            capacity -= thing_weight
            backpack.append(fliped_things[thing_weight])

    print(*backpack)


if __name__ == '__main__':
    func_1(max_weight)
    print()
    func_2(max_weight)
