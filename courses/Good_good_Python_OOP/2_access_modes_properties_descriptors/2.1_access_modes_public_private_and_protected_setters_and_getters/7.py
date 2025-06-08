"""
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров
должно возвращаться значение None, например:
em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):
get_random_email(cls) - для генерации случайного email-адреса по формату:
xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский
буквы, цифры, символ подчеркивания и точка)
check_email(cls, email) - возвращает True, если email записан верно и False -
в противном случае

Корректность строки email определяется по следующим критериям:
- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и
собачка @ (одна)
- длина email до символа @ не должна превышать 100 (сто включительно)
- длина email после символа @ не должна быть больше 50 (включительно)
- после символа @ обязательно должна идти хотя бы одна точка
- не должно быть двух точек подряд

Также в классе нужно реализовать приватный статический метод класса:
is_email_str(email) - для проверки типа переменной email, если строка,
то возвращается значение True, иначе - False

Метод is_email_str() следует использовать в методе check_email() перед
проверкой корректности email. Если параметр email не является строкой,
то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать
не нужно):
res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
"""

import re
import random
import string


class EmailValidator:

    def __new__(cls):
        pass

    @classmethod
    def get_random_email(cls):
        return (
            ''.join(
                random.choice(string.ascii_letters + string.digits + '._')
                for _ in range(random.randint(1, 100))
            ) + '@gmail.com'
        )

    @classmethod
    def check_email(cls, email):
        pattern = re.compile(
            r'(?!.*\.\..*)'             # не должно быть двух точек подряд
            r'[\w\d._]{1,100}'          # длина email до символа @ не должна превышать 100
            r'@'                        # @? @!
            r'(?=.*\.)'                 # после символа @ обязательно должна идти хотя бы одна точка
            r'[\w\d._]{1,50}',          # длина email после символа @ не должна быть больше 50
            flags=re.ASCII
        )

        return (
            True if re.fullmatch(pattern, email) and cls.__is_email_str(email)
            else False
        )

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


random_email = EmailValidator.get_random_email()
print(EmailValidator.get_random_email())
print(EmailValidator.check_email(random_email))
print()
print(EmailValidator.check_email("sc_lib@list.ru"))  # == True
print(EmailValidator.check_email("sc_lib@list_ru"))  # == False
print(EmailValidator.check_email("sc@lib@list_ru"))  # == False
print(EmailValidator.check_email("sc.lib@list_ru"))  # == False
print(EmailValidator.check_email("sclib@list.ru"))  # == True
print(EmailValidator.check_email("sc.lib@listru"))  # == False
print(EmailValidator.check_email("sc..lib@list.ru"))  # == False
