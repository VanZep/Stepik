"""
На вход программе подаются две строки (каждая вводится с новой строки).
Необходимо их прочитать и объединить в одну строку через пробел. Результат
вывести на экран.

Sample Input:
hello python
i love you

Sample Output:
hello python i love you
"""

str_1 = input()
str_2 = input()
print(str_1, str_2)
str_3 = str_1 + ' ' + str_2
print(str_3)
