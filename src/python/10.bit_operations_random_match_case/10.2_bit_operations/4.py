"""
На вход программе подается целое десятичное число. Прочитайте его и, используя
битовые операции, выполните умножение введенного числа на 4. Выведите на экран
полученное числовое значение.

Sample Input:
40

Sample Output:
160
"""

num = int(input())
print(num << 2)
