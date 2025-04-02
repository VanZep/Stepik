"""
Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка
строк из входного потока в формате:
id, name, old, salary (записанные через пробел).
Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

добавить два метода. Первый метод:

insert(self, data) - для добавления в конец списка lst_data новых данных из
переданного списка строк data. При этом, каждый элемент в списке lst_data
должен быть представлен словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например, строка "1 Сергей 35 120000" должна быть преобразована в словарь:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

и только после этого добавляется в список lst_data. И так для всех строк из
переданного списка data в метод insert().

Второй метод:

select(self, a, b) - для возвращения нового списка из элементов существующего
списка lst_data в диапазоне индексов [a; b] (включительно) (не id, а индексам
списка). Следует иметь в виду, что граница b может превышать длину списка.

Примечание: в этой задаче число элементов в строке (разделенных пробелом)
всегда совпадает с числом полей в коллекции FIELDS.

P.S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:

    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for item in data:
            self.lst_data.append(dict(zip(self.FIELDS, item.split())))

    def select(self, a, b):
        return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
print(db.select(0, 0))
