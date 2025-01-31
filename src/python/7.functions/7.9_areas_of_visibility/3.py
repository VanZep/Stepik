"""
Объявите функцию с именем create_global, которая имеет следующую сигнатуру:
def create_global(x): ...
Эта функция должна создавать глобальную переменную с именем TOTAL и
присваивать ей значение x.
"""


def create_global(x):
    """Создаёт глобальную переменную."""
    global TOTAL
    TOTAL = x


if __name__ == '__main__':
    create_global(3)
    print(TOTAL)
