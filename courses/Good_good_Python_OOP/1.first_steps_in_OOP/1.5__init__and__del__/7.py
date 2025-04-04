"""
Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()

Каждый объект класса Cart должен иметь локальное свойство goods - список
объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально
этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора
(TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
Названия и цены придумайте сами.
"""


class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{good.name}: {good.price}' for good in self.goods]


class Good:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Good):
    pass


class TV(Good):
    pass


class Notebook(Good):
    pass


class Cup(Good):
    pass


cart = Cart()
cart.add(TV('Sony', 100000))
cart.add(TV('LG', 80000))
cart.add(Table('Компьютерный стол', 23000))
cart.add(Notebook('ASUS', 90000))
cart.add(Notebook('Lenovo', 60000))
cart.add(Cup('Кружка', 330))
print(cart.get_list())
