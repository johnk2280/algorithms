# Бинарный поиск числа методом рекурсии.
# Функция возвращает только номер позиции искомого числа. Все f - строки убрал.
import timeit
import cProfile


def binary_search(arr, number):
    if not arr:
        return f'\nИскомое число {number} отсутствует в списке'
    else:
        low = 0
        high = len(arr) - 1
        mid_pos = (low + high) // 2
        if arr[mid_pos] == number:
            return mid_pos
        else:
            return binary_search(arr[: mid_pos], number) if arr[mid_pos] > number else (
                    binary_search(arr[mid_pos + 1:], number) + (mid_pos + 1))


spam = [i for i in range(-100000000, 100000000)]
# spam = [-50, -47, -44, -41, -38, -35, -32, -29, -26, -23, -20, -17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22,
# 25, 28, 31, 34, 37, 40, 43, 46, 49]
binary_search(spam, 28)
# print(timeit.timeit('binary_search(spam, 28)'))
# cProfile.run('x=binary_search(spam, 28)')

# ---------------------------cProfile-----------------------------------
# -------------- Список из 30 элементов --------------------------------
#
# 13 function calls (9 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       5/1    0.000    0.000    0.000    0.000 lesson_4_task_1_2.py:7(binary_search)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ---------------------------cProfile-----------------------------------
# ---------------------Список из 2 000 000 элементов --------------------
#
#  45 function calls (25 primitive calls) in 0.017 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#      21/1    0.017    0.001    0.017    0.017 lesson_4_task_1_2.py:7(binary_search)
#         1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#        21    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ---------------------------cProfile-----------------------------------
# ---------------------Список из 20 000 000 элементов --------------------
#          51 function calls (28 primitive calls) in 0.157 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.157    0.157 <string>:1(<module>)
#      24/1    0.157    0.007    0.157    0.157 lesson_4_task_1_2.py:7(binary_search)
#         1    0.000    0.000    0.157    0.157 {built-in method builtins.exec}
#        24    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ---------------------------cProfile-----------------------------------
# # ---------------------Список из 200 000 000 элементов --------------------
#
#    53 function calls (29 primitive calls) in 1.501 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.501    1.501 <string>:1(<module>)
#      25/1    1.501    0.060    1.501    1.501 lesson_4_task_1_2.py:7(binary_search)
#         1    0.000    0.000    1.501    1.501 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ----------------------------Timeit----------------------------------------
# -------------- Список из 30 элементов --------------------------------
# 1) Timeit
# 100 loops, best of 5: 107 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (10.2 usec) was more than four times slower than the best time (107 nsec).

# 2)Timeit
# 1000 loops, best of 5: 77.5 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (743 nsec) was more than four times slower than the best time (77.5 nsec).


# ---------------------Список из 2 000 000 элементов --------------------
# 1)
# 100 loops, best of 5: 77.7 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (741 usec) was more than four times slower than the best time (77.7 nsec).

# 2)
# 1000 loops, best of 5: 74.4 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (72.9 usec) was more than four times slower than the best time (74.4 nsec).


# ---------------------Список из 20 000 000 элементов --------------------

# 3)
# 1000 loops, best of 5: 75.1 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (696 usec) was more than four times slower than the best time (75.1 nsec).