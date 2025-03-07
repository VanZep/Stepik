"""
На вход программе подаются целые числа, записанные через пробел. Необходимо их
прочитать и сохранить в списке. Затем, выполнить сортировку этого списка по
возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать
новый отсортированный список.

Вызовите результирующую функцию сортировки для введенного списка и отобразите
результат на экран в виде последовательности чисел, записанных через пробел.

Подсказка: для разбиения списка и его последующей сборки используйте
рекурсивные функции.

Sample Input:
8 11 -6 3 0 1 1

Sample Output:
-6 0 1 1 3 8 11
"""


def merge(lst_1, lst_2, pointer_1=0, pointer_2=0, new_lst=None):
    """Выплняет сортировку слиянием двух списков."""
    length_1 = len(lst_1)
    length_2 = len(lst_2)
    if new_lst is None:
        new_lst = []
    if length_1 > pointer_1 and length_2 > pointer_2:
        if lst_1[pointer_1] < lst_2[pointer_2]:
            new_lst.append(lst_1[pointer_1])
            pointer_1 += 1
        else:
            new_lst.append(lst_2[pointer_2])
            pointer_2 += 1
        return merge(lst_1, lst_2, pointer_1, pointer_2, new_lst)
    new_lst.extend(lst_1[pointer_1:] + lst_2[pointer_2:])
    return new_lst


def split(lst):
    """Разбивает список, а затем, с помощью функции merge
    собирает новый отсортированный список.
    """
    central_index = len(lst) // 2
    lst_1, lst_2 = lst[:central_index], lst[central_index:]
    if len(lst_1) > 1:
        lst_1 = split(lst_1)
    if len(lst_2) > 1:
        lst_2 = split(lst_2)

    return merge(lst_1, lst_2)


if __name__ == '__main__':
    lst_in = list(map(int, input().split()))
    print(*split(lst_in))
