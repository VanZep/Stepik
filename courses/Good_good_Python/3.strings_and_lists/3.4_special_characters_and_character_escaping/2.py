"""
На вход программе подается строка, состоящая из двух слов, записанных в одну
строчку через пробел. Необходимо прочитать строку и между словами поставить
символ обратного слеша (вместо пробела). Результирующую строку отобразите на
экране.

P.S. Задачу реализовать без применения F-строк.

Sample Input:
Hello Balakirev!

Sample Output:
Hello\Balakirev!
"""

print('\\'.join(input().split()))
