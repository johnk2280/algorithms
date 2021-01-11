# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

#  Вариант 1. Функция по условиям задачи без применения min() и max()
def exchange_in(arr):
    max_el = arr[0]
    min_el = arr[0]
    max_pos = 0
    min_pos = 0
    for i in range(len(arr)):
        if arr[i] > max_el:
            max_el = arr[i]
            max_pos = i
        elif arr[i] < min_el:
            min_el = arr[i]
            min_pos = i
    arr[max_pos], arr[min_pos] = arr[min_pos], arr[max_pos]
    return f'Максимальный значение {max_el} находится на позиции {max_pos}\n' \
           f'Минимальное значение {min_el} находится на позиции {min_pos}\n' \
           f'Список после замены значений {arr}'


# Вариант 2. Функция с применением min() и max()
def exchange_in1(arr):
    a = arr.index(max(arr))
    b = arr.index(min(arr))
    arr[a], arr[b] = arr[b], arr[a]
    return f'Список после замены значений {arr}'


spam = [11, 125, 10, 200, 891, 34, 76, 19, 3, 84]
print(f'Исходный список {spam}')
print(exchange_in(spam))
print(exchange_in1(spam))
