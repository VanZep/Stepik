"""
На вход программе подается строка с числами новых подписчиков канала по дням,
записанных в одну строку через пробел. Необходимо прочитать эти числа и
сохранить в списке, как целые числа в порядке их следования в строке. Затем,
вывести через пробел на экран максимальное, минимальное и суммарное значения
этого списка.

Sample Input:
52 65 64 54 68 59 42 63

Sample Output:
68 42 467
"""

lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))
