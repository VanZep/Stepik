"""
Вам доступен текстовый файл logfile.txt с информацией о времени входа
пользователя в систему и выхода из нее. Каждая строка файла содержит три
значения, разделенные запятыми и символом пробела: имя пользователя, время
входа, время выхода, где время указано в 24-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена
всех пользователей (не меняя порядка следования), которые были в сети не менее
часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием
задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся
в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, то
есть в файле нет двух строк с одинаковым пользователем.

Примечание 3. Если бы файл logfile.txt содержал строки:
Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10

то файл output.txt имел бы вид:
Тимур Гуев
Роман Гацалов
Габолаев Георгий
"""

from datetime import datetime as dt


def is_more_difference_than_one_hour(start, end):
    format = '%H:%M'
    return (
            dt.strptime(end, format) - dt.strptime(start, format)
    ).seconds >= 3600


with (
    open('logfile.txt', 'r', encoding='utf-8') as in_file,
    open('output.txt', 'w', encoding='utf-8') as out_file
):
    for line in in_file.read().split('\n'):
        name, start_time, end_time = line.split(', ')
        if is_more_difference_than_one_hour(start_time, end_time):
            out_file.write(name + '\n')
