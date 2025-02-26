"""
На вход программе подается целое десятичное число. Прочитайте его и, используя
битовые операции, проверьте, включен ли 5-й или 1-й биты введенного числа.
Если включен хотя бы один из этих битов, то выведите слово "ДА",
иначе - слово "НЕТ".

Sample Input:
74

Sample Output:
ДА
"""

num = int(input())
first_bit = 1 << 1
fifth_bit = 1 << 5
print(
    ('НЕТ', 'ДА')[num & first_bit == first_bit or num & fifth_bit == fifth_bit]
)
