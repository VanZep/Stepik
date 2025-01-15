"""
Объявите в программе функцию с одним параметром, которая проверяет
корректность переданного ей email-адреса в виде строки. Полагается,
что адрес верен, если он обязательно содержит символы '@' и '.',
а все остальные символы могут принимать значения:
'a-z', 'A-Z', '0-9' и '_'.
Если email верен, то функция выводит "ДА", иначе "НЕТ".

После объявления функции прочитайте (с помощью функции input)
строку с email-адресом и вызовите функцию с этим аргументом.

Sample Input:
sc_lib@list.ru
маил@что.ru
sc_lib_list.ru
привет@точ_ка.py

Sample Output:
ДА
НЕТ
НЕТ
НЕТ
"""

import re
from string import ascii_letters, digits

EMAIL = input()


def print_is_valid_email_1(email):
    """Проверяет валидность email-адреса."""
    print(
        'ДА'
        if email.count('@') == 1
        and
        email.count('.') == 1
        and
        set(email).issubset(ascii_letters + digits + '@' + '.' + '_')
        else 'НЕТ'
    )


def print_is_valid_email_2(email):
    """Проверяет валидность email-адреса."""
    print(
        'ДА'
        if re.match(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-z]+$', email)
        else 'НЕТ'
    )


if __name__ == '__main__':
    print_is_valid_email_1(EMAIL)
    print()
    print_is_valid_email_2(EMAIL)
