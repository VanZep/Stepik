"""
На вход программе подаются две буквы, записанные через пробел. Необходимо
вывести на экран строку в формате (без кавычек):

"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"

Sample Input:
a z

Sample Output:
Коды: a = 97, z = 122
"""

a, b = input().split()
print(f'Коды: {a} = {ord(a)}, {b} = {ord(b)}')
