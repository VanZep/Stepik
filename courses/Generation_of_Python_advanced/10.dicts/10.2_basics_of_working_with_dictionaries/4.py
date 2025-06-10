"""
Напишите программу, которая будет превращать натуральное число в строку,
заменяя все цифры в числе на слова:
0 на zero
1 на one
2 на two
3 на three
4 на four
5 на five
6 на six
7 на seven
8 на eight
9 на nine

Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести строковое представление числа.

Примечание. Используйте словарь вместо условного оператора.

Тестовые данные

Sample Input 1:
230

Sample Output 1:
two three zero

Sample Input 2:
7

Sample Output 2:
seven

Sample Input 3:
11111111

Sample Output 3:
one one one one one one one one

Sample Input 4:
83

Sample Output 4:
eight three
"""

numbers = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

input_number = input()

print(*(numbers[num] for num in input_number))
