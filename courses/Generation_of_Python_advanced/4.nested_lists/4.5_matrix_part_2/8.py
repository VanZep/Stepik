"""
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает
положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит
конь, отметьте английской буквой N, а клетки, которые бьет конь, отметьте
символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной
нотации (то есть в виде e4, где сначала записывается номер столбца
(буква от a до h, слева направо), затем номеру строки
(цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы
пробелами.

Тестовые данные

Sample Input 1:
b6

Sample Output 1:
* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .

Sample Input 2:
f3

Sample Output 2:
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . * . * .
. . . * . . . *
. . . . . N . .
. . . * . . . *
. . . . * . * .
"""

ROWS = '87654321'
COLS = 'abcdefgh'

cell = input()
size = len(ROWS)
x = ROWS.index(cell[1])
y = COLS.index(cell[0])
board = [['.'] * size for _ in range(size)]
board[x][y] = 'N'

for i in range(size):
    for j in range(size):
        if abs((x - i) * (y - j)) == 2:
            board[i][j] = '*'


for row in board:
    print(*row)
