"""
Дополните приведенный код, используя генератор, так, чтобы получить словарь
result, где ключом будет элемент списка numbers, а значением – отсортированный
по возрастанию список всех его делителей, начиная с 1.

Примечание 1. Если бы список numbers имел вид numbers = [1, 6, 18],
то результатом был бы словарь:
result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
"""

numbers = [
    34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95,
    1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360
]

result = {
    num: [div for div in range(1, num // 2 + 1) if num % div == 0] + [num]
    for num in numbers
}

print(result)
