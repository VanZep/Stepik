"""
На мобильных кнопочных телефонах текстовые сообщения можно отправлять с
помощью цифровой клавиатуры. Поскольку с каждой клавишей связано несколько
букв, для большинства букв требуется несколько нажатий клавиш. При однократном
нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие
цифры 2,3,4 или 5 раз генерирует второй, третий, четвертый или пятый символ
клавиши.

1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
0	space (пробел)

Напишите программу, которая отображает нажатия клавиш, необходимые для
введенного сообщения.

Формат входных данных
На вход программе подается одна строка – текстовое сообщение.

Формат выходных данных
Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.

Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные
буквы.

Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в
приведенной выше таблице.

Примечание 3. Nokia 3310, чтобы вспомнить, как это было 😄

Подсказка
Создайте словарь, в котором каждая буква или символ сопоставляется с нажатиями
клавиш, необходимыми для их создания.

Тестовые данные

Sample Input 1:
Hello, World!

Sample Output 1:
4433555555666110966677755531111

Sample Input 2:
He said: "I can solve this problem".

Sample Output 2:
44330777724443111110444022226607777666555888330844444777707777666225553361

Sample Input 3:
Bee   Geek!!!

Sample Output 3:
2233330004333355111111111111
"""

symbol_button = {
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0'
}


print(''.join(symbol_button.get(symbol, '') for symbol in input().upper()))
