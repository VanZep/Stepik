"""
Напишите программу, которая с помощью модуля random генерирует n паролей
длиной m символов, состоящих из строчных и прописных английских букв и цифр,
кроме тех, которые легко перепутать между собой:
«l» (L маленькое)
«I» (i большое)
«1» (цифра)
«o» и «O» (маленькая и большая буквы)
«0» (цифра)

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести n паролей длиной m символов в соответствии с условием
задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли
сгенерировать возможно.

Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна
цифра и буква в верхнем и нижнем регистре.

Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных
функций:
функция generate_password(length) – возвращает случайный пароль длиной length
символов
функция generate_passwords(count, length) – возвращает список, состоящий из
count случайных паролей длиной length символов

Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа.
Возможны и другие способы генерации паролей.

Тестовые данные

Sample Input 1:
9
7

Sample Output 1:
YbykdW8
heEWSyL
MDxYCzf
syWRujr
mFGBYNJ
bhmg5ip
2XmPgsx
hy7UMVs
JzKPyBw

Sample Input 2:
3
15

Sample Output 2:
itnSA8L3UsBXhWb
82hvi7yFBWjw6fg
hSd6V3CxyHvgw2m

Sample Input 3:
20
4

Sample Output 3:
QcLR
d8Xj
85dQ
aXr4
cuVj
38Dx
sd4Q
bkrA
tb96
p6Gg
neVN
AvQJ
4fzr
X68L
Lwxr
j8gQ
aR5Q
QCq4
a9Qm
Az4M
"""

from string import ascii_letters, digits
from random import choices

chars_for_password = tuple(set(ascii_letters).union(digits) - set('lIOo10'))


def generate_password(length):
    return ''.join(choices(chars_for_password, k=length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')
