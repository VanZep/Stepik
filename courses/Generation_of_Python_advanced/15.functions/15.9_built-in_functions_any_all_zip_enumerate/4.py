"""
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети,
работающей по протоколу TCP/IP.

В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в
виде четырёх десятичных чисел (октетов) со значением от 0 до 255
(включительно), разделённых точками, например, 192.168.1.2.

Напишите программу с использованием встроенной функции all() для проверки
корректности IP-адреса: все ли октеты в IP-адресе – числа со значением от 0 до
255.

Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор
символов 0-9, a-z.

Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и
False в противном случае.

Примечание. Ведущие нули следует игнорировать:
0001 = 1
006 = 6
0213 = 213
0000 = 0
00345 = 345
...

Тестовые данные

Sample Input 1:
10.0.1.1

Sample Output 1:
True

Sample Input 2:
10.1.1.a

Sample Output 2:
False

Sample Input 3:
10.1.1.260

Sample Output 3:
False

Sample Input 4:
10.0023.0123.0000015

Sample Output 4:
True
"""

print(all(
    item.isdigit() and 0 <= int(item) < 256 for item in input().split('.')
))
