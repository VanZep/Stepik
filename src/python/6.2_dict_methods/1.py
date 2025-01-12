"""
На вход программе подается строка из русских букв и символов пробела.
Необходимо ее прочитать и закодировать азбукой Морзе, где каждой букве ставится
в соответствие код из точки и тире. После каждой закодированной буквы должен
стоять пробел (символ окончания кода буквы). После последнего кода пробела быть
не должно (в конце строки). Коды азбуки Морзе приведены ниже для русского
алфавита и символа пробела:
d = {
    ' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
    'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....',
    'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--',
    'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
}
Результат кодирования вывести в виде строки.

Sample Input:
Сергей Балакирев

Sample Output:
... . .-. --. . .--- -...- -... .- .-.. .- -.- .. .-. . .--
"""

d = {
    ' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
    'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....',
    'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--',
    'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
}

print(*(d.get(i.upper()) for i in input()))