"""
На вход программе подается строка. Необходимо ее прочитать и в ней заменить
кириллические символы на соответствующие латинские обозначения (без учета
регистра букв), а все остальные символы - на символ дефиса (-). Для этого в
программе уже объявлен словарь:
t = {
    'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}
Используя его, примените функцию map, которая бы выдавала преобразованные
фрагменты для входной строки. На основе этой функции сформируйте строку,
состоящую из преобразованных фрагментов (фрагменты в строке должны идти друг
за другом без пробелов). Отобразите результат на экране.

Sample Input:
Привет Питон

Sample Output:
privet-piton
"""

t = {
    'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}
str_in = input()
result_str = ''.join(map(lambda x: t.get(x, '-'), str_in.lower()))
print(result_str)
