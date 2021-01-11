# Вывод всех простых чисел до n.
# Решето Эратосфена, пока один самых быстрых алгоритмов.

import cProfile

# n = int(input('До какого целого числа получить простые числа?: '))
n = 1000


def find_prime(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]


cProfile.run('find_prime(n)')
# spam = [i for i in result if i % 2 == 0]
# print(result)
# print(spam)


# -----------------------Timeit-------------------------
# ---------------------до 1 000 -------------------------
# 1000 loops, best of 5: 95.3 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (1.07 usec) was more than four times slower than the best time (95.3 nsec).

# ---------------------до 1 000 000 -------------------------
# 1000 loops, best of 5: 61.1 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (509 usec) was more than four times slower than the best time (61.1 nsec).


# --------------------cProfile------------------------------
#
# ---------------------до 1 000 -------------------------
#          6 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 sieve.py:18(<listcomp>)
#         1    0.000    0.000    0.001    0.001 sieve.py:8(find_prime)
#         1    0.000    0.000    0.000    0.000 sieve.py:9(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ---------------------до 1 000 000 -------------------------
#          6 function calls in 0.413 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.006    0.006    0.413    0.413 <string>:1(<module>)
#         1    0.024    0.024    0.024    0.024 sieve.py:18(<listcomp>)
#         1    0.344    0.344    0.408    0.408 sieve.py:8(find_prime)
#         1    0.040    0.040    0.040    0.040 sieve.py:9(<listcomp>)
#         1    0.000    0.000    0.413    0.413 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}