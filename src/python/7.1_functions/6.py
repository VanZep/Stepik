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

Sample Output:
ДА
"""

from string import ascii_letters, digits

EMAIL = input()


def email_validator(email):
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


if __name__ == '__main__':
    email_validator(EMAIL)
