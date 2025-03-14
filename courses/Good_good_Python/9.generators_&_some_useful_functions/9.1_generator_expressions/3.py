"""
На вход программе поступают два целых числа a и b (a < b), записанные в одну
строчку через пробел. Определите генератор, который бы выдавал модули целых
чисел из диапазона [a; b] (включительно). В цикле выведите первые пять значений
этого генератора. Каждое значение с новой строки. (Гарантируется, что пять
значений имеются).

Sample Input:
-3 3

Sample Output:
3
2
1
0
1
"""

a, b = map(int, input().split())
gen = (abs(x) for x in range(a, b + 1))
print(*(next(gen) for _ in range(5)), sep='\n')
