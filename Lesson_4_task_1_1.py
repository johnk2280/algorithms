# Бинарный поиск числа при помощи цикла while.
# Функция возвращает только номер позиции искомого числа. Все f - строки убрал.
import timeit
import cProfile


def bin_search(arr, number):
    bottom = 0
    top = len(arr) - 1
    while bottom <= top:
        middle_pos = (bottom + top) // 2
        if arr[middle_pos] == number:
            return middle_pos
        elif arr[middle_pos] > number:
            top = middle_pos - 1
        else:
            bottom = middle_pos + 1
    return number


# spam = [i for i in range(-100000000, 100000000)]
# spam = [-50, -47, -44, -41, -38, -35, -32, -29, -26, -23, -20, -17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22,
#         25, 28, 31, 34, 37, 40, 43, 46, 49]
# bin_search(spam, 28)
# print(timeit.timeit('x = bin_search(spam, 28)'))
# cProfile.run('bin_search(spam, 45)')

# ---------------------------cProfile-----------------------------------
# -------------- Список из 30 элементов --------------------------------
#
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1_1.py:7(bin_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ---------------------------cProfile-----------------------------------
# ---------------------Список из 2 000 000 элементов --------------------
#
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1_1.py:7(bin_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# # ---------------------------cProfile-----------------------------------
# # ---------------------Список из 20 000 000 элементов --------------------
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1_1.py:7(bin_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ----------------------------------Timeit-----------------------------------------------------
# ---------------------------Список из 30 элементов--------------------------------------------
#
# "lesson_4_task_1_1.bin_search([i for i in range(-50, 50, 3)], 28)"
# 1000 loops, best of 5: 1.83 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (5.35 msec) was more than four times slower than the best time (1.83 usec)

# ---------------------Список из 20 000 элементов --------------------
# "lesson_4_task_1_1.bin_search([i for i in range(-10000, 10000)], 28)"
# 1000 loops, best of 5: 529 usec per loop
