"""
Реализуйте односвязный список (не список Python, не использовать список Python
для хранения объектов), когда один объект ссылается на следующий и так по
цепочке до последнего.

Для этого объявите в программе два класса:
StackObj - для описания объектов односвязного списка
Stack - для управления односвязным списком

Объекты класса StackObj предполагается создавать командой:
obj = StackObj(данные)

Здесь данные - это строка с некоторым содержимым. Каждый объект класса
StackObj должен иметь следующие локальные приватные атрибуты:
__data - ссылка на строку с данными, указанными при создании объекта
__next - ссылка на следующий объект класса StackObj (при создании объекта
принимает значение None)

Также в классе StackObj должны быть объявлены объекты-свойства:
next - для записи и считывания информации из локального приватного свойства
__next
data - для записи и считывания информации из локального приватного свойства
__data

При записи необходимо реализовать проверку, что __next будет ссылаться на
объект класса StackObj или значение None. Если проверка не проходит,
то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:
st = Stack() # создание объекта односвязного списка

В объектах класса Stack должен быть локальный публичный атрибут:
top - ссылка на первый добавленный объект односвязного списка (если список
пуст, то top = None).

А в самом классе Stack следующие методы:
push(self, obj) - добавление объекта класса StackObj в конец односвязного
списка
pop(self) - извлечение последнего объекта с его удалением из односвязного
списка
get_data(self) - получение списка из объектов односвязного списка (список из
строк локального атрибута __data каждого объекта в порядке их добавления, или
пустой список, если объектов нет)

Пример использования классов Stack и StackObj (эти строчки в программе писать
не нужно):
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
"""


class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        self.__next = next_obj


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, obj):
        if not self.top:
            self.top = self.bottom = obj
        else:
            self.bottom.next = obj
            self.bottom = obj

    def pop(self):
        if not self.bottom:
            return None

        deleted = self.bottom

        if self.top.next:
            prev_bottom = self.top
            while prev_bottom.next.next:
                prev_bottom = prev_bottom.next
            self.bottom = prev_bottom
            self.bottom.next = None
        else:
            self.top = self.bottom = None

        return deleted

    def get_data(self):
        data = []
        top = self.top
        while top:
            data.append(top.data)
            top = top.next

        return data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
st.pop()
st.push(StackObj("obj4"))
res = st.get_data()
print(res)
