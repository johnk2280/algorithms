# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import cProfile


size = 20
eggs = [round(random.uniform(0, 50), 2) for _ in range(size)]
spam = eggs.copy()

print(f'Исходный список: {eggs}')

"""
Рекурсивный алгоритм сортировки слиянием разбит на две функции для удобства восприятия:
на функцию разбиения исходного списка и функцию слияния. 
"""


def merge_sort(arr):
    """
    Функция принимает исходный список и возвращает отсортированный.
    Внутри функции мы рекурсивно разбиваем исходный список целочисленно на 2,
    до тех пор, пока список не будет состоять из одного элемента.
    Список из одного элемента является отсортированным.
    Далее для двух списков вызываем функцию слияния merge().
    """
    if len(arr) == 1:
        return arr
    mid_pos = len(arr) // 2
    left = merge_sort(arr[:mid_pos])
    right = merge_sort(arr[mid_pos:])
    return merge(left, right)


def merge(arr1, arr2):
    """
    Функция сравнивает каждый элемент левого и правого списков поочередно.
    И добавляет наименьший в список-результат.
    Можно обойтись без дополнительного списка и все выполнить одной функцией.
    """
    result = []
    i, j = 0, 0
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    while i < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len_arr1:
        result.append(arr1[i])
        i += 1

    while j < len_arr2:
        result.append(arr2[j])
        j += 1

    return result


print(f'Результат сортировки слиянием: {merge_sort(spam)}')

# cProfile.run('merge_sort(spam)')

# ------------------------200 000 элементов----------------------------------------------------------------------------
#          5137853 function calls (4737855 primitive calls) in 1.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    1.015    1.015 <string>:1(<module>)
#  399999/1    0.175    0.000    1.014    1.014 task_2.py:18(merge_sort)
#    199999    0.640    0.000    0.814    0.000 task_2.py:27(merge)
#         1    0.000    0.000    1.015    1.015 {built-in method builtins.exec}
#    999996    0.043    0.000    0.043    0.000 {built-in method builtins.len}
#   3537856    0.156    0.000    0.156    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ------------------------1 000 000 элементоов--------------------------------------------------------------------------
# 27951421 function calls (25951423 primitive calls) in 5.588 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.004    0.004    5.588    5.588 <string>:1(<module>)
# 1999999/1    0.913    0.000    5.585    5.585 task_2.py:20(merge_sort)
#    999999    3.587    0.000    4.542    0.000 task_2.py:36(merge)
#         1    0.000    0.000    5.588    5.588 {built-in method builtins.exec}
#   4999996    0.217    0.000    0.217    0.000 {built-in method builtins.len}
#  19951424    0.868    0.000    0.868    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
