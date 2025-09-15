"""
Напишите программу, которая считывает одну строку текста и выводит 10 строк,
пронумерованных от 0 до 9 каждая, с указанной строкой текста.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести 10 строк в соответствии с условием задачи.

Тестовые данные

Sample Input 1:
LeBron

Sample Output 1:
0 LeBron
1 LeBron
2 LeBron
3 LeBron
4 LeBron
5 LeBron
6 LeBron
7 LeBron
8 LeBron
9 LeBron

Sample Input 2:
Roman

Sample Output 2:
0 Roman
1 Roman
2 Roman
3 Roman
4 Roman
5 Roman
6 Roman
7 Roman
8 Roman
9 Roman
"""

name = input()

for i in range(10):
    print(i, name)
