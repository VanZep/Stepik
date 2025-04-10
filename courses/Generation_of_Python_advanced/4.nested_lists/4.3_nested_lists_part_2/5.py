"""
На вход программе подается строка текста, содержащая символы. Напишите
программу, которая упаковывает последовательности одинаковых символов заданной
строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, разделенные
символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Тестовые данные

Sample Input 1:
a b c d

Sample Output 1:
[['a'], ['b'], ['c'], ['d']]

Sample Input 2:
w w w o r l d g g g g r e a t t e c c h e m g g p w w

Sample Output 2:
[
    ['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'],
    ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'],
    ['g', 'g'], ['p'], ['w', 'w']
]

Sample Input 3:
g i v e t h h i i s m a a a n a g u u n
g i v e t h h i i s m a a a n a g u u u

Sample Output 3:
[
    ['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'],
    ['a', 'a', 'a'], ['n'], ['a'], ['g'], ['u', 'u'], ['n']
]
"""

# 1-е решение
chars = input().split()
packed_chars = []
pack = [chars[0]]

for i in range(1, len(chars)):
    current = chars[i]
    if pack[-1] == current:
        pack.append(current)
    else:
        packed_chars.append(pack)
        pack = [current]
else:
    packed_chars.append(pack)

print(packed_chars)

# 2-е решение
chars = input().split()
packed_chars = [[chars.pop(0)]]

for char in chars:
    pack = packed_chars[-1]
    if char in pack:
        pack.append(char)
    else:
        packed_chars.append([char])

print(packed_chars)
