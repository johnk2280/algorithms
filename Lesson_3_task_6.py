# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random


# Вариант 1.
def get_sum(arr):
    max_el = arr[0]
    min_el = arr[0]
    max_pos = 0
    min_pos = 0
    for pos, value in enumerate(arr):
        if value > max_el:
            max_el = value
            max_pos = pos
        if value < min_el:
            min_el = value
            min_pos = pos
    if min_pos < max_pos:
        return sum(arr[min_pos + 1:max_pos])
    elif min_pos > max_pos:
        return sum(arr[max_pos + 1:min_pos])


# Вариант 2.
def get_sum1(arr):
    temp_list = [arr.index(min(arr)), arr.index(max(arr))]
    return sum([arr[i] for i in range(len(arr)) if min(temp_list) < i < max(temp_list)])


spam = [random.randint(-100, 100) for _ in range(0, 20)]
# spam = [170, 57, 18, -45, -9, 21, 20, -71, -62, 88, -98, -66, 68, 9, -3, 51, 11, 80, 14, 22]
print(f'Сгенерированный массив {spam}')
print('---Вариант 1---')
print(f'Сумма значений между минимальным и максимальным значением равна {get_sum(spam)}')
print('---Вариант 2---')
print(f'Сумма значений между минимальным и максимальным значением равна {get_sum1(spam)}')
