"""
Объявите класс с именем ShopItem (товар), объекты которого создаются командой:
item = ShopItem(name, weight, price)

где name - название товара (строка)
weight - вес товара (число: целое или вещественное)
price - цена товара (число: целое или вещественное)

Определите в этом классе магические методы:
__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и
ценой имели бы равные хэши
__eq__() - чтобы объекты с одинаковыми хэшами были равны

Затем, из входного потока прочитайте строки командой:
lst_in = list(map(str.strip, sys.stdin.readlines()))

Строки имеют следующий формат:
название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса
ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны
выступать сами объекты, а значениями - список в формате:
[item, total]
где item - объект класса ShopItem
total - общее количество одинаковых объектов (с одинаковыми хэшами)

Подумайте, как эффективно программно наполнять такой словарь, проходя по
списку lst_in один раз.

P.S. На экран ничего выводить не нужно, только объявить класс и сформировать
словарь.

Sample Input:
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Sample Output:

"""

from __future__ import annotations
import sys

Digit = int | float


class ShopItem:

    def __init__(self, name: str, weight: Digit, price: Digit) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key: str, value: str | Digit) -> None:
        if key in ('weight', 'price'):
            if type(value) != int and not isinstance(value, float):
                raise TypeError(f'Аттрибут {key} должен быть int или float')
        super().__setattr__(key, value)

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other: ShopItem) -> bool:
        self.check_shop_item(other)
        return hash(self) == hash(other)

    @staticmethod
    def check_shop_item(obj: ShopItem) -> None:
        if not isinstance(obj, ShopItem):
            raise TypeError('Сравниваемым должен быть объект класса ShopItem')


lst_in: list[str] = list(map(str.strip, sys.stdin.readlines()))
shop_items: dict[ShopItem: [ShopItem, int]] = {}

for item in lst_in:
    name, weight_price = item.split(':')
    attrs = []
    for attr in weight_price.split():
        if '.' in attr:
            attr = float(attr)
        else:
            attr = int(attr)

        attrs.append(attr)

    shop_item = ShopItem(name, *attrs)
    shop_items.setdefault(shop_item, [shop_item, 0])[1] += 1
