"""
На вход программе подается вещественное число. Необходимо его прочитать,
импортировать только одну функцию floor из модуля math, вызывать ее для
прочитанного числа и отобразить результат на экране.

Sample Input:
8.11

Sample Output:
8
"""
from math import floor

if __name__ == '__main__':
    float_num = float(input())
    print(floor(float_num))
