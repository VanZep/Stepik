"""
Допишите текст программы для нахождения минимального значения из пяти
введенных целых чисел с выводом результата в консоль (минимального значения) с
помощью функции print.
"""

d1, d2, d3, d4, d5 = map(int, input().split())
print(min(d1, d2, d3, d4, d5))
