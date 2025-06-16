"""
Анаграмма – слово (словосочетание), образованное путем перестановки букв,
составляющих другое слово (или словосочетание). Например, английские слова
evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет,
являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES, если слова являются анаграммами, или NO в
противном случае.

Тестовые данные

Sample Input 1:
thing
night

Sample Output 1:
YES

Sample Input 2:
cat
rat

Sample Output 2:
NO

Sample Input 3:
tea
eat

Sample Output 3:
YES
"""

char_count_dicts = ({}, {})

for dct in char_count_dicts:
    for ch in input().lower():
        dct[ch] = dct.get(ch, 0) + 1

print(('NO', 'YES')[char_count_dicts[0] == char_count_dicts[1]])
