"""
На вход программе подается строка. Прочитайте эту строку и отобразите на
экране ее первый и последний символ (подряд в одну строчку).

Sample Input:
I love Python

Sample Output:
In
"""

s = input()
print(s[0] + s[-1])
