"""
На вход программе подаются два целых числа a и b (a < b), записанные в одну
строчку через пробел. Необходимо их прочитать и сформировать список lst из
целых чисел в диапазоне от a до b (включительно) с шагом 1, используя функцию
range, оператор [] и оператор распаковки *. Вывести полученный список на
экран командой:
print(*lst)

Sample Input:
3 11

Sample Output:
3 4 5 6 7 8 9 10 11
"""

a, b = map(int, input().split())
lst = [*range(a, b + 1)]
print(*lst)
