# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
#   a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#   b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#
#   Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import cProfile

size = 10
eggs = [random.randrange(-100, 100) for _ in range(size)]
spam = eggs.copy()

print(f'Исходный список: {eggs}')


def bubble_sort1(arr):
    """Класическая сортировка пузырьком по убыванию."""
    n = 1
    while n <= len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
        print(arr)
    return arr


def bubble_sort2(arr):
    """
    Оптимизированная сортировка пузырьком по убыванию.
    Здесь добавлена проверка на факт проведения замены.
    Если замены в цикле не происходило, то цикл завершается прнудительно, и функция возращает результат.
    """
    n = 1
    is_exit = True
    while is_exit:
        is_exit = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_exit = True
        if not is_exit:
            break
        n += 1
        print(arr)
    return arr


print(f'Классическая сортировка пузырьком по убыванию:     {bubble_sort1(eggs)}')
print(f'Оптимизированная сортировка пузырьком по убыванию: {bubble_sort2(spam)}')


# cProfile.run('bubble_sort1(eggs)')
# cProfile.run('bubble_sort2(spam)')

# Не смотря н оптимизацию, оптимизированная функция работате чуть медленнее.
# 20005 function calls in 5.134 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.134    5.134 <string>:1(<module>)
#         1    5.133    5.133    5.134    5.134 task_1.py:19(bubble_sort1)
#         1    0.000    0.000    5.134    5.134 {built-in method builtins.exec}
#     20001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          9904 function calls in 5.187 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.187    5.187 <string>:1(<module>)
#         1    5.187    5.187    5.187    5.187 task_1.py:31(bubble_sort2)
#         1    0.000    0.000    5.187    5.187 {built-in method builtins.exec}
#      9900    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
