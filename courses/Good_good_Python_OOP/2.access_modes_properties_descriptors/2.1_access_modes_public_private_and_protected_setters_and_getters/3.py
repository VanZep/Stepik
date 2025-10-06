"""
Объявите класс Book со следующим набором сеттеров и геттеров:
set_title(self, title) - запись в локальное приватное свойство __title
объектов класса Book значения title
set_author(self, author) - запись в локальное приватное свойство __author
объектов класса Book значения author
set_price(self, price) - запись в локальное приватное свойство __price
объектов класса Book значения price
get_title(self) - получение значения локального приватного свойства __title
объектов класса Book
get_author(self) - получение значения локального приватного свойства __author
объектов класса Book
get_price(self) - получение значения локального приватного свойства __price
объектов класса Book

Объекты класса Book предполагается создавать командой:
book = Book(автор, название, цена)

При этом, в каждом объекте должны создаваться приватные локальные свойства:
__author - строка с именем автора
__title - строка с названием книги
__price - целое число с ценой книги
"""


class Book:

    def __init__(self, author, title, price):
        self.set_author(author)
        self.set_title(title)
        self.set_price(price)

    def set_author(self, author):
        self.__author = author if isinstance(author, str) else None

    def set_title(self, title):
        self.__title = title if isinstance(title, str) else None

    def set_price(self, price):
        self.__price = price if isinstance(price, (int, float)) else None

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price


book = Book('Балакирев', 'Python ООП', 100)
print(book.get_author(), book.get_title(), book.get_price(), sep='\n')
