"""
На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку
выбором полученного списка по возрастанию (неубыванию). Идея алгоритма очень
проста и проиллюстрирована на рисунке pictures/6.png.

Вначале мы рассматриваем первый элемент списка и ищем второй минимальный
относительно первого элемента (включая и его). На рисунке - это последний
элемент со значением -1. Затем, меняем местами первый и последний элементы.
Переходим ко второму элементу списка и повторяем эту же процедуру, но
относительно второго элемента (то есть, первый уже не рассматриваем).
На рисунке минимальный элемент - это 2, поэтому менять местами здесь ничего
не нужно. Переходим к 3-му элементы со значением 6. Относительно него находим
минимальный элемент - это 3. Меняем их местами.

Вот идея алгоритма сортировки выбором. Реализуйте его для сформированного
списка целых чисел. Результат выведите на экран в виде последовательности
чисел, записанных в одну строчку через пробел.

Sample Input:
8 11 -53 2 10 11

Sample Output:
-53 2 8 10 11 11
"""

# Моё решение
lst = list(map(int, input().split()))
for i, num in enumerate(lst):
    lst_slice = lst[i:]
    min_num = min(lst_slice)
    index_min_num = lst_slice.index(min_num) + i
    lst[index_min_num], lst[i] = num, min_num

print(*lst)

# Доработанное решение
lst_2 = list(map(int, input().split()))
for i, num in enumerate(lst_2):
    index_min_num = lst_2.index(min(lst_2[i:]), i, len(lst_2))
    lst_2[index_min_num], lst_2[i] = num, lst_2[index_min_num]

print(*lst_2)

# Другой вариант
lst_3 = list(map(int, input().split()))
lst_3_length = len(lst_3)
for i in range(lst_3_length):
    for j in range(i + 1, lst_3_length):
        x = lst_3[i]
        y = lst_3[j]
        if x <= y:
            continue
        else:
            lst_3[i], lst_3[j] = y, x
print(*lst_3)

# Ещё вариант
lst_4 = list(map(int, input().split()))
lst_length = len(lst_4)
for i in range(lst_length):
    for j in range(i + 1, lst_length):
        if lst_4[i] <= lst_4[j]:
            continue
        else:
            lst_4[i], lst_4[j] = lst_4[j], lst_4[i]
print(*lst_4)
