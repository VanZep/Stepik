"""
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов,
содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со
встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном
случае.

Тестовые данные

Sample Input 1:
abcABC9

Sample Output 1:
YES

Sample Input 2:
abAB34

Sample Output 2:
NO

Sample Input 3:
DFSDFSDFSDsdfjsdfnsm

Sample Output 3:
NO
"""

from string import ascii_lowercase, ascii_uppercase, digits

password = input()

print(
    ('NO', 'YES')[all([
        any(ch in ascii_uppercase for ch in password),
        any(ch in ascii_lowercase for ch in password),
        any(ch in digits for ch in password),
        len(password) > 6
    ])]
)
