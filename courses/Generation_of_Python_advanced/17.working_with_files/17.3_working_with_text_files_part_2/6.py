"""
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу,
которая выводит количество букв латинского алфавита, слов и строк. Выведите
три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

то результатом было бы:
Input file contains:
108 letters
20 words
4 lines

Примечание 2. Словом называется последовательность из непробельных символов.
Например, строка abc a21 67pop    qwert bo7ok 83456
содержит 6 слов: abc, a21, 67pop, qwert, bo7ok, 83456.
"""

from string import punctuation, digits

with open('file.txt') as file:
    data = file.read()

letters_count = len(
    ''.join(word.strip(punctuation + digits) for word in data.split())
)
words_count = len(data.split())
lines_count = len(data.split('\n'))
print(
    'Input file contains:',
    f'{letters_count} letters',
    f'{words_count} words',
    f'{lines_count} lines',
    sep='\n'
)
