"""
Напишите программу для вывода общего количества уникальных символов во всех
считанных словах без учета регистра.

Формат входных данных
На вход программе в первой строке подается число n – общее количество слов.
Далее идут n строк со словами.

Формат выходных данных
Программа должна вывести одно число – общее количество уникальных символов во
всех словах без учета регистра.

Тестовые данные

Sample Input 1:
5
aAa
bB
ccc
dDdd
ppppP

Sample Output 1:
5

Sample Input 2:
4
авТорИтет
небо
машинА
Мёд

Sample Output 2:
13

Sample Input 3:
4
троС
рОст
сорт
тОрС

Sample Output 3:
4
"""

# 1-ое решение
string = ''

for _ in range(int(input())):
    string += input()

print(len(set(string.lower())))


# 2-ое решение
set_result = set()

for _ in range(int(input())):
    set_result.add(input().lower())

print(len(set_result))
