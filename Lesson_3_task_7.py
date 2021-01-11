# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random


def get_min(arr):
    a = min(arr)
    return a, min([el for el in arr if el != a])


spam = [random.randint(-100, 100) for _ in range(0, 20)]
# spam = [170, 57, 18, -45, -9, 21, 20, -71, -62, 88, -98, -66, 68, 9, -3, 51, 11, 80, 14, 22]
print(f'Сгенерированный массив {spam}')
print(get_min(spam))
