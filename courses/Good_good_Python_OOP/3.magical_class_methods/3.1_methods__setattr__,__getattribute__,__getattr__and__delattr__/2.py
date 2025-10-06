"""
Вы создаете интернет-магазин. Для этого нужно объявить два класса:
Shop - класс для управления магазином в целом
Product - класс для представления отдельного товара

Объекты класса Shop следует создавать командой:
shop = Shop(название магазина)

В каждом объекте класса Shop должно создаваться локальное свойство:
goods - список товаров (изначально список пустой).

А также в классе объявить методы:
add_product(self, product) - добавление нового товара в магазин (в конец
списка goods)
remove_product(self, product) - удаление товара product из магазина (из списка
goods)

Объекты класса Product следует создавать командой:
p = Product(название, вес, цена)

В них автоматически должны формироваться локальные атрибуты:
id - уникальный идентификационный номер товара (генерируется автоматически как
целое положительное число от 1 и далее)
name - название товара (строка)
weight - вес товара (целое или вещественное положительное число)
price - цена (целое или вещественное положительное число)

В классе Product через магические методы (подумайте какие) осуществить
проверку на тип присваиваемых данных локальным атрибутам объектов класса
(например, id - целое число, name - строка и т.п.). Если проверка не проходит,
то генерировать исключение командой:
raise TypeError("Неверный тип присваиваемых данных.")

Также в классе Product с помощью магического(их) метода(ов) запретить удаление
локального атрибута id. При попытке это сделать генерировать исключение:
raise AttributeError("Атрибут id удалять запрещено.")

Пример использования классов (в программе эти строчки не писать):
shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")


P.S. На экран ничего выводить не нужно.
"""


class Shop:

    def __init__(self, title):
        self.title = title
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id: (int,)
    name: (str,)
    weight: (int, float)
    price: (int, float)

    id_counter = 0

    def __init__(self, name, weight, price):
        self.id = self.get_id()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def get_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def __setattr__(self, key, value):
        if type(value) not in self.__annotations__.get(key) or (
                type(value) in (int, float) and value <= 0
        ):
            raise TypeError('Неверный тип присваиваемых данных.')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено.')
        super().__delattr__(item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

del book.id
