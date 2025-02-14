"""
Объявите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну
строчку через пробел.
"""


def get_prime_num():
    """Функция-генератор. Возвращает простые числа."""
    a = 2
    while True:
        for b in range(2, a):
            if a % b == 0:
                break
        else:
            yield a
        a += 1


if __name__ == '__main__':
    gen = get_prime_num()
    print(*(next(gen) for _ in range(20)))
