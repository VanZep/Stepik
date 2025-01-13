"""
Объявите в программе функцию, которая имеет один параметр - вес предмета,
и выводит на экран сообщение (без кавычек):
"Предмет имеет вес: x кг."

где x - переданное значение (аргумент) функции. После объявления функции
прочитайте (с помощью функции input) вещественное число и вызовите функцию
с этим числовым значением.

Sample Input:
12.67

Sample Output:
Предмет имеет вес: 12.67 кг.
"""

item_weight = float(input())


def print_message(weight):
    """Принимает вес и выводит в консоль сообщение."""
    print(f'Предмет имеет вес: {weight} кг.')


if __name__ == '__main__':
    print_message(item_weight)
