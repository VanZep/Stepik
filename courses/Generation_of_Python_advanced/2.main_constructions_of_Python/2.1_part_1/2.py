"""
Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
ИМТ показывает, человек весит больше или меньше нормы для своего роста.
ИМТ человека рассчитывают по формуле:

ИМТ=масса(кг)/рост(м)*рост(м),
где масса измеряется в килограммах, а рост – в метрах.

Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25.
Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
Если значение ИМТ больше 25, то считается, что человек весит больше нормы.

Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и
25 (включительно). "Недостаточная масса", если ИМТ меньше 18.5 и
"Избыточная масса", если значение ИМТ больше 25.

Формат входных данных
На вход программе подается два числа: масса и рост человека, каждое на
отдельной строке. Все входные числа являются действительными, используйте для
них тип данных float.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные

Sample Input 1:
65
1.75

Sample Output 1:
Оптимальная масса

Sample Input 2:
80
2.23

Sample Output 2:
Недостаточная масса

Sample Input 3:
80
1.6

Sample Output 3:
Избыточная масса
"""

LOWER_LIMIT = 18.5
HIGHER_LIMIT = 25


def calculate_body_mass_index(weight, height):
    """Вычисляет индекс массы тела."""
    return weight / height ** 2


def compare_body_mass_index(body_mass_index):
    """Сравнивает индекс массы тела со стандартными значениями
    и формирует сообщение.
    """
    if body_mass_index < LOWER_LIMIT:
        message = 'Недостаточная масса'
    elif body_mass_index > HIGHER_LIMIT:
        message = 'Избыточная масса'
    else:
        message = 'Оптимальная масса'
    return message


if __name__ == '__main__':
    weight = float(input())
    height = float(input())
    body_mass_index = calculate_body_mass_index(weight, height)
    result_message = compare_body_mass_index(body_mass_index)
    print(result_message)
