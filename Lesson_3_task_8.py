# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


# Вариант 1. С использованием sum().
def sum_row1(listoflists):
    for line in listoflists:
        line.append(sum(line))
        for item in line:
            print(f'{item:^4}', end='')
        print()


# # Вариант 2. Без использования sum().
def sum_row2(listoflists):
    for line in listoflists:
        sum_line = 0
        for item in line:
            sum_line += item
        line.append(sum_line)
        for item in line:
            print(f'{item:^4}', end='')
        print()


matrix = []
for i in range(5):
    row = list(map(int, input(f'Line {i}: enter four numbers separated by a space: ').split()))
    matrix.append(row)

# matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 0, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
# matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 0, 9], [8, 7, 6, 5], [4, 3, 2, 1]]

print(f'List of lists: {matrix}')

print('Source matrix:')
for row in matrix:
    for el in row:
        print(f'{el:>4}', end='')
    print()

print('The resulting matrix:')
print('---Version 1---')
sum_row1(matrix)

#  Т.к. первая функция изменяет исходную матрицу (список списков),
#  то вторая функция выводит матрицу размером 5х6.
print('---Version 2---')
sum_row2(matrix)
