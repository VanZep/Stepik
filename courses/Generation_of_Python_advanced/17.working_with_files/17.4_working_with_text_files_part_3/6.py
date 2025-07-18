"""
На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt и выводит в него
содержимое всех файлов, не меняя их порядка.

Формат входных данных
На вход программе подаются натуральное число n и n строк названий существующих
файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием
задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся
в одной папке.

Примечание 2. Если бы на вход было подано 2 файла и эти файлы содержали бы
строки (обратите внимание, что в конце первого файла нет перевода строки):
Early in the morning

и

we
went
for mushrooms

то результирующий файл output.txt выглядел бы следующим образом:

Early in the morningwe
went
for mushrooms
"""

file_names = [input() for _ in range(int(input()))]

all_files_data = ''
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        all_files_data += file.read()

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(all_files_data)
