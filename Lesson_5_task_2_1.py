# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

# ------------------------------Данный вариант не совсем корректный----------------------------------------------------


def convert_to_decimal(arr):
    """Функция перевода из 16-ричной системы в 10-чную"""
    number = 0
    exponent = len(arr)
    for i in range(exponent):
        exponent -= 1
        number += arr[i] * (16 ** exponent)
    return number


def exchange_to_decimal(arr):
    """Функция перевода цифр 16-ричного алфавита в 10-чный."""
    return [hex_dict.get(key) for key in arr]


def convert_to_hex(number):
    result = deque()
    for i in range(len(str(number))):
        result.appendleft(number % 16)
        number //= 16
    return result


def exchange_to_hex(arr):
    """Фуекция перевода значений списка из 10-тичного алфавита в 16-тиричный"""
    return [get_key(hex_dict)[el] for el in arr]


def get_key(some_dict):
    """Фуекция смены местами ключей и значений словаря"""
    result_dict = {some_dict.get(key): key for key in some_dict.keys()}
    return result_dict


hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

a = input(f'Enter the 1st hex-number: ')
b = input(f'Enter the 2nd hex-number: ')

list_a = exchange_to_decimal(a)
list_b = exchange_to_decimal(b)

decimal_a = convert_to_decimal(list_a)
decimal_b = convert_to_decimal(list_b)

sum_num = decimal_a + decimal_b
multi_num = decimal_a * decimal_b

result_sum = convert_to_hex(sum_num)
result_multi = convert_to_hex(multi_num)

n = ''.join(exchange_to_hex(result_sum))
m = ''.join(exchange_to_hex(result_multi))
print(n, m)

