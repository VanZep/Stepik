"""
Вам поручается создать программу по учету книг (библиотеку). Для этого
необходимо в программе объявить два класса:
Lib - для представления библиотеки в целом
Book - для описания отдельной книги

Объекты класса Book должны создаваться командой:
book = Book(title, author, year)

где title - заголовок книги (строка)
author - автор книги (строка)
year - год издания (целое число)

Объекты класса Lib создаются командой:
lib = Lib()

Каждый объект должен содержать локальный публичный атрибут:
book_list - ссылка на список из книг (объектов класса Book). Изначально список
пустой.

Также объекты класса Lib должны работать со следующими операторами:
lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по
ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет
начинается с нуля)
lib -= indx

При реализации бинарных операторов + и - создавать копии библиотек (объекты
класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:
n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.

P.S. В программе достаточно только объявить классы. На экран ничего выводить
не нужно.
"""

from typing import List, Union


class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class Lib:

    def __init__(self) -> None:
        self.book_list: List[Book] = []

    def __add__(self, other: Book) -> 'Lib':
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __iadd__(self, other: Book) -> 'Lib':
        return self.__add__(other)

    def __sub__(self, other: Union[Book, int]) -> 'Lib':
        if isinstance(other, Book):
            if other in self.book_list:
                self.book_list.remove(other)
        elif type(other) is int:
            if self.__len__() > other:
                self.book_list.pop(other)
        else:
            raise TypeError('Неверный тип данных')

        return self

    def __isub__(self, other: Union[Book, int]) -> 'Lib':
        return self.__sub__(other)

    def __len__(self) -> int:
        return len(self.book_list)


book = Book('title', 'author', 'year')
book2 = Book('title2', 'author2', 'year2')
lib = Lib()

print(lib.book_list)

lib = lib + book  # добавление новой книги в библиотеку
lib += book2

print(lib.book_list)

lib = lib - book  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book2

print(lib.book_list)

lib = lib - 2  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 2

print(lib.book_list)

n = len(lib)  # n - число книг

print(n)
