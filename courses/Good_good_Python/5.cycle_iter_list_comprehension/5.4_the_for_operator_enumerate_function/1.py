"""
На вход программе подается строка. Необходимо ее прочитать и найти в ней все
индексы строкового фрагмента "ра". Выведите найденные индексы на экран в одну
строчку через пробел. Если же фрагмент "ра" отсутствует в строке, то вывести
-1.

Sample Input:
Барабанщик бил бой в барабан

Sample Output:
2 23
"""

s = input().lower()

if 'ра' in s:
    for i, char in enumerate(s):
        if s[i: i + 2] == 'ра':
            print(i, end=' ')
else:
    print(-1)
