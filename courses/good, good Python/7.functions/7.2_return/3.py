"""
Объявите функцию с именем is_large, которая принимает строку
(в качестве параметра) и возвращает булево значение False, если длина
строки меньше трех символов, иначе True.

Sample Input:
Я люблю Python!

Sample Output:
True
"""

word = input()


def is_large(string):
    """Возвращает False, если длина строки меньше трех символов, иначе True."""
    return len(string) > 2


if __name__ == '__main__':
    print(is_large(word))
