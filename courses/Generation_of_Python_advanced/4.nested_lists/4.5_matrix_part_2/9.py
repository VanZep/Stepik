"""
Магическим квадратом порядка n называется квадратная таблица размера n×n,
составленная из всех чисел 1,2,3, …, n**2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой. Напишите
программу, которая проверяет, является ли заданная квадратная матрица
магическим квадратом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в
матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделенные
пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом,
или NO в противном случае.

Тестовые данные

Sample Input 1:
3
8 1 6
3 5 7
4 9 2

Sample Output 1:
YES

Sample Input 2:
3
8 2 6
3 5 7
4 9 1

Sample Output 2:
NO

Sample Input 3:
3
4 9 2
3 5 7
8 1 6

Sample Output 3:
YES
"""

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
summ = sum(matrix[0])


def is_equal_row_and_col_sums():
    trans_matrix = list(zip(*matrix))
    is_equal_sums = True

    for mtx in (matrix, trans_matrix):
        for row in mtx:
            if summ != sum(row):
                is_equal_sums = False
                break

    return is_equal_sums


def is_equal_diag_sums():
    major_diag_summ = 0
    secondary_diag_summ = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                major_diag_summ += matrix[i][j]
            if n - 1 - i == j:
                secondary_diag_summ += matrix[i][j]

    return summ == major_diag_summ == secondary_diag_summ


def is_unique_elements():
    unique_elements = set()

    for row in matrix:
        unique_elements.update(row)

    return len(unique_elements) == n**2


def is_in_range_values():
    min_value = 1
    max_value = n**2
    success_check = True

    for row in matrix:
        for value in row:
            if not min_value <= value <= max_value:
                success_check = False

    return success_check


def main():
    check_functions = (
        is_equal_row_and_col_sums,
        is_equal_diag_sums,
        is_unique_elements,
        is_in_range_values
    )
    for function in check_functions:
        if not function():
            print('NO')
            break
    else:
        print('YES')


if __name__ == '__main__':
    main()
