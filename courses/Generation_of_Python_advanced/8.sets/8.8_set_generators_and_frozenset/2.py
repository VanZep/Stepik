"""
Используя генератор множеств, дополните приведенный ниже код так, чтобы
получить множество, содержащее первую букву каждого слова (в нижнем регистре)
списка words. Результат вывести на одной строке в алфавитном порядке, разделяя
элементы одним символом пробела.
"""

words = [
    'Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate',
    'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
    'tangerine', 'Watermelon', 'currant', 'Almond'
]
myset = {word[0].lower() for word in words}

print(*sorted(myset))
