# Evgeniy Kungurov
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input('Enter the number of numbers: '))
i = 1
max_sum = 0
while i <= n:
    sum_num = 0
    number = input('Enter the processed number: ')
    num = int(number)
    i += 1
    for j in range(len(number)):
        sum_num += num % 10
        num //= 10
    if sum_num > max_sum:
        max_sum = sum_num
        max_num = number
    print(f'The number {max_num} has the maximum sum - {max_sum}')
print('Exit to program')
