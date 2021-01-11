# Evgeniy Kungurov
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    question = input('Enter the data (Y / N)? ')
    if question.upper() == 'N':
        print('Exit the program.')
        break
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    sign = input('Enter the operator: ')
    if sign == '+':
        print(f'The sum of the numbers is {a + b}')
    elif sign == '-':
        print(f'The difference in numbers is {a - b}')
    elif sign == '*':
        print(f'The multiply of the number is {a * b}')
    elif sign == '/':
        if int(b) == 0:
            print('Division by zero!!!')
        else:
            print(f'The division of numbers is {a / b}')
    else:
        print('Incorrect value!')


