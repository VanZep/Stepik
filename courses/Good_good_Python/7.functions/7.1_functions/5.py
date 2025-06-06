"""
Объявите в программе функцию с двумя параметрами width и height
(ширина и высота прямоугольника), которая выводит сообщение (без кавычек):
"Периметр прямоугольника, равен x"

где x - вычисленный периметр прямоугольника. После объявления функции
прочитайте (с помощью функции input) два целых числа, записанных в одну строку
через пробел, и вызовите функцию с этими числовыми значениями.

Sample Input:
8 11

Sample Output:
Периметр прямоугольника, равен 38
"""

WIDTH, HEIGHT = map(int, input().split())


def print_rectangle_perimeter(width, height):
    """Принимает ширину и высоту, и выводит в консоль сообщение."""
    print(f'Периметр прямоугольника, равен {(width + height) * 2}')


if __name__ == '__main__':
    print_rectangle_perimeter(WIDTH, HEIGHT)
