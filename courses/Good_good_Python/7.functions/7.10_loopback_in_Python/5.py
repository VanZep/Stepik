"""
Реализуйте в программе следующее замыкание функций. Объявите внешнюю функцию с
одним параметром tp, в который будет передаваться тип коллекции (строка).
В теле внешней функции объявите вложенную функцию с одним параметром, которая
преобразует строку (переданную через параметр) с набором целых чисел,
записанных через пробел, либо в список, либо в кортеж. Тип коллекции
определяется параметром tp внешней функции. Если tp = 'list', то используется
список, иначе (при другом значении) - кортеж. При этом внешняя функция должна
возвращать ссылку на вложенную функцию.

Далее, на вход программы поступают две строки: первая - это значение для
параметра tp; вторая - последовательность целых чисел, записанных через пробел.
Прочитайте их и с помощью реализованного замыкания преобразуйте эти данные в
соответствующую коллекцию. Результат работы вложенной функции (сохраненный
через переменную lst) выведите на экран командой:
print(lst)

Обратите внимание, что в возвращаемой коллекции должны присутствовать числа,
а не их строковые представления.

Sample Input:
list
-5 6 8 11 0 111 -456 3

Sample Output:
[-5, 6, 8, 11, 0, 111, -456, 3]
"""


def make_list_or_tuple(tp):
    """Принимает параметр tp и возвращает
    ссылку на внутреннюю функцию.
    """

    def list_or_tuple(nums_str):
        """Преобразует строку с числами в список или кортеж."""
        nums_map = map(int, nums_str.split())
        return list(nums_map) if tp == 'list' else tuple(nums_map)

    return list_or_tuple


if __name__ == '__main__':
    typ = input()
    nums_string = input()
    nums = make_list_or_tuple(typ)
    print(nums(nums_string))
