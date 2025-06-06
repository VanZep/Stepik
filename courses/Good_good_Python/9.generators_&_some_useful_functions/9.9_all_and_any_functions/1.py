"""
На вход программе подаются целые числа, записанные через пробел. Необходимо их
прочитать и определить, являются ли все эти числа четными. Вывести True, если
это так и False в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
2 4 6 8 22 56

Sample Output:
True
"""

nums = list(map(int, input().split()))
print(all(map(lambda x: x % 2 == 0, nums)))
print(all(num % 2 == 0 for num in nums))
