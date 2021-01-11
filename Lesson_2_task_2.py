# Evgeniy Kungurov
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Enter an integer: '))
i, j = 0, 0
while num > 0:
    m = num % 10
    num //= 10
    if m % 2 == 0:
        i += 1
    else:
        j += 1
print(f'Even digits in a number: {i}')
print(f'Odd digits in a number: {j}')

