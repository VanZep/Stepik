"""
На вход программе подается строка. Прочитайте ее и отобразите все ее символы с
нечетными индексами (подряд в одну строчку).

Sample Input:
Balakirev

Sample Output:
aaie
"""

s = input()
print(s[1::2])
