# Evgeniy Kungurov
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
s = ''
num = int(input('Enter an integer: '))
while num > 0:
    m = num % 10
    num //= 10
    s += str(m)
print(f'Revers number: {s}')
