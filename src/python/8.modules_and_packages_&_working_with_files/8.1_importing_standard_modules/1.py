"""
На вход программе подается вещественное число. Необходимо его прочитать,
импортировать модуль math, вызывать функцию ceil модуля math для
прочитанного числа и отобразить результат на экране.

Sample Input:
5.67

Sample Output:
6
"""
from math import ceil

if __name__ == '__main__':
    float_num = float(input())
    print(ceil(float_num))
