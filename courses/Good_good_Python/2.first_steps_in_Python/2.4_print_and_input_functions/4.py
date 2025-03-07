"""
В программе вводятся строки в переменные s1 и s2. Необходимо их отобразить в
консоли в формате:
Word 1: s1 | Word 2: s2

Например, если s1 = "abc"; s2 = "defsg", то выводится строка:
Word 1: abc | Word 2: defsg

Sample Input:
I love

Sample Output:
Word 1: I | Word 2: love
"""

s1, s2 = map(str.strip, input().split())
print(f'Word 1: {s1}', f'Word 2: {s2}', sep=' | ')
