"""
На вход программе подается строка из двух слов, записанных через пробел.
Необходимо прочитать эту строку и сформировать новую строку, продублировав
первое слово дважды, а второе - трижды (все слова в результирующей строке
должны идти через пробел). Результат выведите на экран.

Программу следует реализовать без использования F-строк, с применением
оператора дублирования строк.

Sample Input:
hello python

Sample Output:
hello hello python python python
"""

a, b = input().split()
print((a + " ") * 2 + (b + " ") * 3)
