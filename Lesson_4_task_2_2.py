# Вывод всех простых чисел до n.
# Намеренно сделал алгоритм медленным, что бы можно было сравнить с решетом.
# При n = 1 000 000 в данном решениии процесс пришлось убить принудительно, т.к. вентилятор грозил вырваться наружу.

import cProfile
import timeit

n = 100000
odds = [i for i in range(1, n + 1) if
        i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 9 != 0 and i % 9 != 0 and i % 11 != 0]
odds[0] = 11
primes = [2, 3, 5, 7]


def find_prime(arr):
    result = []
    for i in range(len(arr)):
        for j in range(2, i + 1):
            if arr[i] % j == 0:
                result.append(arr[i])
    return sorted(list(set(arr) - set(result)))


primes.extend(find_prime(odds))
cProfile.run('find_prime(odds)')
# print(primes)


# -----------------------Timeit-------------------------
# ---------------------до 1 000 -------------------------
# $ python3 -m timeit -n 1000 "import find_prime"
# 1000 loops, best of 5: 96.9 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (2.36 usec) was more than four times slower than the best time (96.9 nsec).


# ---------------------до 100 000 -------------------------
# 1000 loops, best of 5: 65.1 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (11.3 msec) was more than four times slower than the best time (65.1 nsec).


# --------------------cProfile------------------------------
#
# ---------------------до 1 000 -------------------------
#
#          86 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 find_prime.py:11(find_prime)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#        80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#
# ---------------------до 100 000 -------------------------
# при n = 1 000 000 пришлось убить процесс
#
#          27885 function calls in 11.607 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   11.607   11.607 <string>:1(<module>)
#         1   11.605   11.605   11.607   11.607 find_prime.py:11(find_prime)
#         1    0.000    0.000   11.607   11.607 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#     27879    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#