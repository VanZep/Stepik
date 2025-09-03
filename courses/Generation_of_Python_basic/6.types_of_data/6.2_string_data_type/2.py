"""
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию
пользователя – и выводит фразу:
Hello <введённое имя> <введённая фамилия>! You have just delved into Python

Формат входных данных
На вход программе подаются две строки (имя и фамилия), каждая на отдельной
строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные

Sample Input 1:
Anthony
Joshua

Sample Output 1:
Hello Anthony Joshua! You have just delved into Python

Sample Input 2:
Michael
Jordan

Sample Output 2:
Hello Michael Jordan! You have just delved into Python

Sample Input 3:
Leonardo
DiCaprio

Sample Output 3:
Hello Leonardo DiCaprio! You have just delved into Python
"""

name, surname = input(), input()

print(f'Hello {name} {surname}! You have just delved into Python')
