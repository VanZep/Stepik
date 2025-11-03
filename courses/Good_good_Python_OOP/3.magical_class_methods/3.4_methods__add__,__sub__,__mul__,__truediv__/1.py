"""
Известно, что в Python мы можем соединять два списка между собой с помощью
оператора +:
lst = [1, 2, 3] + [4.5, -3.6, 0.78]

Но нет реализации оператора -, который бы убирал из списка соответствующие
значения вычитаемого списка, как это показано в примере:
lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования
оставшихся элементов списка должен сохраняться)

Давайте это поправим и создадим такой функционал. Для этого нужно объявить
класс с именем NewList, объекты которого создаются командами:
lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями

Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами
класса NewList можно было выполнять следующие действия:
lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

Также в классе NewList необходимо объявить метод:
get_list() - для возвращения результирующего списка объекта класса NewList

Например:
lst = res_2.get_list() # [1, 2, 3]


P.S. В программе требуется только объявить класс. На экран ничего выводить
не нужно.
"""


class NewList:

    def __init__(self, lst=None):
        self.__lst = lst if lst and isinstance(lst, list) else []

    def __sub__(self, other):
        # if not
        other = other.__lst if isinstance(other, NewList) else other

        return NewList(self.diff_list(other, self.__lst))

    def __rsub__(self, other):
        return NewList(self.diff_list(self.__lst, other))

    def get_list(self):
        return self.__lst

    @staticmethod
    def diff_list(lst_1, lst_2):
        lst_2_copy = lst_2.copy()
        for i in lst_1:
            for j in range(len(lst_2_copy)):
                if i == lst_2_copy[j] and type(i) == type(lst_2_copy[j]):
                    lst_2_copy[j] = None
                    break

        return list(filter(lambda x: x is not None, lst_2_copy))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
print(a.get_list())
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.get_list())
