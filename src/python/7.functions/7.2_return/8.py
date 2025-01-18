"""
Объявите функцию, которая имеет один параметр, принимающий строку. Функция
должна возвращать два значения в виде кортежа: переданную строку и ее длину.

После объявления функции далее в программе прочитайте из входного потока
строку с названиями городов, записанных через пробел. Сформируйте на основе
прочитанной строки список cities из названий городов. Затем, используя
генератор словарей и ранее объявленную функцию, сформируйте на основе списка
cities словарь d в формате:
d = {<город 1>: <число символов>, ..., <город N>: <число символов>}

Выведите этот словарь в порядке возрастания длин строк с помощью команд:
a = sorted(d, key=d.get)
print(*a)

Sample Input:
Воронеж Лондон Тверь Омск Уфа

Sample Output:
Уфа Омск Тверь Лондон Воронеж
"""


def get_string_and_length(string):
    """Возвращает строку и длинну строки."""
    return string, len(string)


def main():
    """Основная функция."""
    cities = list(map(str.strip, input().split()))
    d = {
        get_string_and_length(city)[0]: get_string_and_length(city)[1]
        for city in cities
    }
    print(*sorted(d, key=d.get))


if __name__ == '__main__':
    main()
