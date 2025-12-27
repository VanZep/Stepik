"""
Имеется стихотворение, представленное следующим списком строк:
stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня."
]

Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в
конце каждого слова и разбить строку по словам (слова разделяются одним или
несколькими пробелами). На основе полученного списка слов, создать объект
класса StringText командой:
st = StringText(lst_words)
где lst_words - список из слов одной строчки стихотворения.

С объектами класса StringText должны быть реализованы операторы сравнения:
st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2

Все объекты класса StringText (для каждой строчки стихотворения) сохранить в
списке lst_text. Затем, сформировать новый список lst_text_sorted из
отсортированных объектов класса StringText по убыванию числа слов. Для
сортировки использовать стандартную функцию sorted() языка Python. После этого
преобразовать данный список (lst_text_sorted) в список из строк (объекты
заменяются на соответствующие строки, между словами ставится пробел).

P.S. На экран в программе ничего выводить не нужно.
"""

import re
from typing import Union


stich = [
    'Я к вам пишу – чего же боле?',
    'Что я могу еще сказать?',
    'Теперь, я знаю, в вашей воле',
    'Меня презреньем наказать.',
    'Но вы, к моей несчастной доле',
    'Хоть каплю жалости храня,',
    'Вы не оставите меня.'
]


class StringText:

    def __init__(self, lst_words: Union[str, list, tuple, set, dict]) -> None:
        self.init_validator(lst_words)
        self.lst_words = list(lst_words)

    def __len__(self) -> int:
        return len(self.lst_words)

    def __lt__(self, other: 'StringText') -> bool:
        self.obj_validator(other)
        return self.__len__() < len(other)

    def __gt__(self, other: 'StringText') -> bool:
        self.obj_validator(other)
        return self.__len__() > len(other)

    def __le__(self, other: 'StringText') -> bool:
        self.obj_validator(other)
        return self.__len__() <= len(other)

    def __ge__(self, other: 'StringText') -> bool:
        self.obj_validator(other)
        return self.__len__() >= len(other)

    def obj_validator(self, obj: 'StringText') -> None:
        if not isinstance(obj, type(self)):
            raise TypeError('Неверный тип данных')

    @staticmethod
    def init_validator(value) -> None:
        if isinstance(value, (int, float, bool)):
            raise TypeError('Значение не может быть: int, float, bool')


# Вариант 1
lst_text = []
for lst in (item.split() for item in stich):
    lst_fomatted = []
    for word in lst:
        word = word.strip('–?!,.;')
        if word:
            lst_fomatted.append(word)
    lst_text.append(StringText(lst_fomatted))

# Вариант 2
stich_parsed = [re.findall(r'\w+', line) for line in stich]
lst_text = [StringText(item) for item in stich_parsed]
print(lst_text)

# Вариант 3
lst_text = [
    StringText(
        [word.strip('–?!,.;') for word in line.split() if word.strip('–?!,.;')]
    ) for line in stich
]


lst_text_sorted = sorted(lst_text, key=len, reverse=True)
lst_text_sorted = [' '.join(item.lst_words) for item in lst_text_sorted]
