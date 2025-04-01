"""
Имеется следующий класс для считывания информации из входного потока:

import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

Которым, затем, можно воспользоваться следующим образом:

sr = StreamReader()
data, result = sr.readlines()

Необходимо перед классом StreamReader объявить еще один класс StreamData с
методом:

def create(self, fields, lst_values): ...

который бы на входе получал кортеж FIELDS из названий локальных атрибутов
(передается в атрибут fields) и список строк lst_in (передается в атрибут
lst_values) и формировал бы в объекте класса StreamData локальные свойства с
именами полей из fields и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает
True, иначе - False. Если число полей и число строк не совпадает, то метод
create() возвращает False и локальные атрибуты создавать не нужно.

P.S. В программе нужно дополнительно объявить только класс StreamData.
Больше ничего делать не нужно.

Пример входной информации (Sample Input):
10
Питон - основы мастерства
512
"""

import sys


class StreamData:

    @staticmethod
    def is_equal_length(fields, lst_values):
        return len(fields) == len(lst_values)

    def create(self, fields, lst_values):
        if self.is_equal_length(fields, lst_values):
            self.__dict__.update(dict(zip(fields, lst_values)))
            return True
        return False


class StreamReader:

    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__, result)
