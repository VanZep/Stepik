"""
Дополните приведенный код, используя генератор, так, чтобы получить словарь
result, в котором ключом будет строка – элемент списка words, а значением –
список соответствующих кодов ASCII символов данной строки.

Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'],
то результатом был бы словарь:
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
"""

words = [
    'hello', 'bye', 'yes', 'no', 'python',
    'apple', 'maybe', 'stepik', 'beegeek'
]

result = {word: [ord(char) for char in word] for word in words}

print(result)
