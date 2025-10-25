"""
Объявите класс LinkedList (связный список).

Здесь создается список из связанных между собой объектов класса ObjList.
Объекты этого класса создаются командой:
obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса
ObjList должны создаваться следующие локальные атрибуты:
__data - ссылка на строку с данными
__prev - ссылка на предыдущий объект связного списка (если объекта нет,
то __prev = None)
__next - ссылка на следующий объект связного списка (если объекта нет,
то __next = None)

В свою очередь, объекты класса LinkedList должны создаваться командой:
linked_lst = LinkedList()
и содержать локальные атрибуты:
head - ссылка на первый объект связного списка (если список пуст,
то head = None)
tail - ссылка на последний объект связного списка (если список пуст,
то tail = None)

А сам класс содержать следующие методы:
add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного
списка
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его
порядковому номеру (индексу); индекс отсчитывается с нуля

Также с объектами класса LinkedList должны поддерживаться следующие операции:
len(linked_lst) - возвращает число объектов в связном списке
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса
ObjList, расположенного под индексом indx (в связном списке)

Пример использования классов (эти строчки в программе писать не нужно):
linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev


P.S. На экран в программе ничего выводить не нужно.
"""


class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        obj = self.get_obj(indx)

        if obj.prev:
            if not obj.next:
                self.tail = obj.prev
            obj.prev.next = obj.next
        elif obj.next:
            if not obj.prev:
                self.head = obj.next
            obj.next.prev = obj.prev
        else:
            self.head = self.tail = None

    def get_obj(self, indx):
        obj = self.head
        for _ in range(indx):
            obj = obj.next

        if not obj:
            raise IndexError('Объекта под таким индексом не существует.')

        return obj

    def __len__(self):
        count = 0
        obj = self.head
        while obj:
            count += 1
            obj = obj.next

        return count

    def __call__(self, indx, *args, **kwds):
        return self.get_obj(indx).data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1)  # s = Balakirev
print(s)
