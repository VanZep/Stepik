"""
На вход программы подаются два целых положительных числа n и m, записанных
через пробел, причем, n < m. Необходимо прочитать эти числа и вывести в одну
строку через пробел квадраты целых чисел в диапазоне [n; m]. Программу
реализовать при помощи цикла while.

Sample Input:
2 4

Sample Output:
4 9 16
"""

n, m = map(int, input().split())
while n <= m:
    print(n ** 2, end=' ')
    n += 1
