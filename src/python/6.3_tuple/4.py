"""
На вход программе подается строка с именами студентов, записанных через
пробел. Необходимо прочитать эту строку и на ее основе сформировать кортеж из
имен. Затем, отобразите на экране все имена малыми буквами из этого кортежа
(по порядку), которые содержат фрагмент "ва" (без учета регистра). Имена
выводятся в одну строчку через пробел в нижнем регистре (малыми буквами).

Sample Input:
Петя Варвара Венера Василиса Василий Федор

Sample Output:
варвара василиса василий
"""

print(*(name.lower() for name in tuple(input().split()) if name.lower().count('ва')))