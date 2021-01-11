# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random


# Вариант 1. Функция возвращает только первое вхождение максимального отрицательного числа и его позицию.
def get_max_negative(arr):
    max_negative = -100
    pos_mn = 0
    for pos, val in enumerate(arr):
        if 0 > val > max_negative:
            max_negative = val
            pos_mn = pos
            spam[pos] = val
    return f'Максимальное отрицательное число {max_negative} с индексом {pos_mn}\n'


# Вариант 2. Возвращает словарь со  всеми вхождениями искомого числа.
def get_max_negative2(arr):
    temp_dict = {i: arr[i] for i in range(len(arr)) if arr[i] < 0}
    return {f'На позиции {key}': f'искомое число {value}' for key, value in temp_dict.items() if
            value == max(temp_dict.values())}


# Вариант 3. Как вариант 2, только без промежуточного словаря. Здесь генератор временного списка
# вставлен в генератор словаря-результата.
def get_max_negative3(arr):
    return {pos: val for pos, val in enumerate(arr) if val == max([el for el in arr if el < 0])}


spam = [random.randint(-100, 100) for _ in range(0, 20)]
print(f'Сгенерированный массив {spam}')
print('---Вариант 1---')
print(get_max_negative(spam))
print('---Вариант 2---')
print(get_max_negative2(spam))
print('---Вариант 3---')
print(get_max_negative3(spam))