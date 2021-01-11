# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


# Вариант 1. Без применения встроенных функций для определения min.
def find_max(listoflists):
    max_number = 0
    # Создаем промежуточный список состоящий из макисмального значения listoflists
    list_min = [max([max(el) for el in listoflists])] * len(listoflists[0])
    for line in listoflists:
        for i, item in enumerate(line):
            # В цикле сравниваем очередное значение ячейки матрицы i-того столбца
            # с i-тым значением промежуточного списка list_min и если меньше, то заменяем значение в списке.
            if item < list_min[i]:
                list_min[i] = item
    print(f'Мимнимальные числа в столбцах:')
    for num in list_min:
        print(f'{num:^4}', end='')
    # Здесь в цикле ищем максимальное значение среди минимальных значенией столбцов
    for el in list_min:
        if el > max_number:
            max_number = el
    print(f'\nМаксимальный элемент среди\nминимальных элементов столбцов => {max_number}')


# Вариант 2.
def find_max2(listoflists):
    max_number = max([max(el) for el in listoflists])
    min_list = [max_number] * len(listoflists[0])
    for line in listoflists:
        for i, item in enumerate(line):
            if item < min_list[i]:
                min_list[i] = item
    return f'Максимальный элемент среди\nминимальных элементов столбцов => {max(min_list)}'


matrix = [[random.randint(1, 20) for _ in range(5)] for _ in range(4)]

print('Исходная матрица:')
for row in matrix:
    for el in row:
        print(f'{el:^4}', end='')
    print()

print('----Вариант 1----')
find_max(matrix)
print('----Вариант 2----')
print(find_max2(matrix))