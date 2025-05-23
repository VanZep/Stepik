"""
Дана строка, состоящая из слов, разделенных пробелами. Напишите программу,
которая подсчитывает количество слов в этой строке.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести количество слов в строке.

Примечание 1. Кроме слов в тексте могут присутствовать только пробелы
(один или несколько).

Примечание 2. Решите задачу в одну строчку кода. 😎

Тестовые данные

Sample Input 1:
Hello world

Sample Output 1:
2

Sample Input 2:
Timur forever young

Sample Output 2:
3

Sample Input 3:
The future belongs to those who believe in beauty of their dreams

Sample Output 3:
12
"""

print(len(input().split()))
