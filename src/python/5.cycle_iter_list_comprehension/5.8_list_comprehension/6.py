"""
На вход программе подается натуральное число N. Необходимо его прочитать и
сгенерировать вложенный список с помощью list comprehension, размером N x N,
где первая строка содержала бы все нули, вторая - все единицы, третья - все
двойки и так до N-й строки. Результат вывести в виде таблицы чисел, как
показано в примере ниже.

Sample Input:
4

Sample Output:
0 0 0 0
1 1 1 1
2 2 2 2
3 3 3 3
"""

N = int(input())
[print(*[i] * N) for i in range(N)]
