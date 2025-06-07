"""
Используя генератор множеств, дополните приведенный ниже код так, чтобы он
выбрал из списка files уникальные имена файлов c расширением .png, независимо
от регистра имен и расширений. Имена файлов вывести вместе с расширением, все
на одной строке, в нижнем регистре, в алфавитном порядке через пробел.

Примечание. Если бы список files содержал следующие имена файлов:

files = [
    'python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',
    'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG'
]
то ответом был бы:
apple.png python.png zebra.png
"""

files = [
    'python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp',
    'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg',
    'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop',
    'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git'
]

unique_files = {
    file_name.lower() for file_name in files
    if file_name.lower().endswith('.png')
}

print(*sorted(unique_files))
