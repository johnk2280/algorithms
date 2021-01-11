# Evgeniy Kungurov
# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

i, j = 0, 1
num = int(input('Enter the number of numbers in the row: '))
for n in range(num):
    print(f'j = {j}')
    i += j
    j /= -2
print(f'The sum of the numbers in the row: {i}')
