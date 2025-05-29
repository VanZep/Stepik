"""
Напишите программу для определения общего количества различных слов в строке
текста.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести одно число – общее количество различных слов в строке
без учета регистра.

Примечание 1. Словом считается последовательность непробельных символов,
идущих подряд, слова разделены одним или большим числом пробелов.

Примечание 2. Знаками препинания .,;:-?! пренебрегаем.

Тестовые данные

Sample Input 1:
Milk is white and so is glue, Ghosts are white and they say BOO!

Sample Output 1:
11

Sample Input 2:
Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.

Sample Output 2:
15

Sample Input 3:
Lets make the color pink. Lets make the color pink. Mixing red and white, I think, Well make the color pink.

Sample Output 3:
12
"""

print(len({word.lower().strip('.,;:-?!') for word in input().split()}))
