"""
На вход программе подается список целых чисел, записанных в одну строчку через
пробел. Необходимо их прочитать и сохранить в виде списка. Затем, с помощью
словаря выделите только уникальные (не повторяющиеся) числа. Сформируйте из них
еще один список (уникальных чисел). Числа в этом списке должны идти в том же
порядке, что и при чтении (из входного потока). Выведите уникальные числа на
экран в одну строчку через пробел.

Sample Input:
8 11 -4 5 2 11 4 8

Sample Output:
8 11 -4 5 2 4
"""

print(*dict.fromkeys(input().split()))