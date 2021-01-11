# Evgeniy Kungurov
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Enter the number of numbers: '))
digit = int(input('Enter the required digit: '))
i = 1

while i <= n:
    count = 0
    number = input('Enter the processed number: ')
    num = int(number)
    for j in range(len(number)):
        if num % 10 == digit:
            count += 1
        num //= 10
    i += 1
    print(f'Number {number} contains {count} digits {digit}')
print('Exit to program')
