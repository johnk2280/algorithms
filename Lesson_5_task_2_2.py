# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
# -------------------------------Корректный вариант--------------------------------------------------------------------


def exchange_to_decimal(arr):
    """Функция перевода цифр 16-ричного алфавита в 10-чный."""

    if not arr:
        return None
    return [hex_dict.get(key) for key in arr]


def exchange_to_hex(arr):
    """Фуекция перевода значений списка из 10-тичного алфавита в 16-тиричный."""

    if not arr:
        return None
    return [decimal_list[el] for el in arr]


def get_sum(arr1, arr2):
    """Функция вычесления суммы двух чисел переведенных в писок."""

    if not arr1:
        return deque(arr2)
    if not arr2:
        return deque(arr1)

    """Изменяем тип со списка list на очередь deque."""

    first = deque(arr1)
    second = deque(arr2)

    """
    Проверка длины списка. Если список arr2 длиннее arr1, меняем их местами. 
    Как того требует правило умножения столбиком.
    """

    if len(second) > len(first):
        first, second = second, first

        """Добавляем 0 в начало очереди в количестве равном разнице длин очередей."""

        second.appendleft(0 * (len(first) - len(second)))
    elif len(second) < len(first):
        second.appendleft(0 * (len(first) - len(second)))

    """Создаем переменную buffer для перенесения разрядов."""

    buffer = 0
    spam = deque()
    # temp_sum = 0

    """
    Цикл для операции сложения.
    Цикл запускаем в реверсивном порядке до -1, т.к. может оставаться разряд в buffer.
    """

    for i in range(len(first) - 1, -1, -1):
        temp_sum = first[i] + second[i] + buffer
        buffer = 0
        if temp_sum >= 16:
            spam.appendleft(temp_sum - 16)
            buffer += 1
        else:
            spam.appendleft(temp_sum)

    """
    Проверяем на оставшийся разряд в buffer. 
    Если buffer == 1, то переносим ее в начало очереди, тем самым увеличивая разряд результата.
    """

    if buffer == 1:
        spam.appendleft(buffer)
    return spam


def get_multi(arr1, arr2):
    """Функция вычесления произведения двух чисел переведенных в список."""

    if not arr1 or not arr2:
        return 0

    """Изменяем тип со списка list на очередь deque"""

    first = deque(arr1)
    second = deque(arr2)

    """
    Проверка длины списка. Если список arr2 длиннее arr1, меняем их местами. 
    Как того требует правило умножения столбиком
    """

    if len(second) > len(first):
        first, second = second, first

    """Цикл для операции умножения."""

    count = 0
    result = []
    for s in reversed(second):

        """
        Создаем переменную buffer для переноса разрядов. 
        И очередь spam, в которой будем накапливать 
        результат поочередного перемножения одного числа из second с каждым из first.
        """

        count += 1
        buffer = 0
        spam = deque()
        for f in reversed(first):
            temp_multi = s * f + buffer
            if temp_multi >= 16:
                spam.appendleft(temp_multi % 16)
                buffer = temp_multi // 16
            else:
                spam.appendleft(temp_multi)
                buffer = 0
        if buffer > 0:
            spam.appendleft(buffer)

        """
        Суммируем результаты перемножений первых двух чисел.
        Если промежуточный результат является не самым первым, то добавляем в конец очереди такое количество нулей, 
        которым по счету является промежкточный список. 
        Это видно из правила по умножению столбиком.
        """

        if count > 1:
            for c in range(1, count):
                spam.append(0)

        """Суммируем промежуточный результат spam с конечным результатом с помощью функции get_sum()."""

        result = get_sum(result, list(spam))

    return result


decimal_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# a = 'A2'
# b = 'C4F'

a = input('Enter the hex-number "a": ')
b = input('Enter the hex-number "b": ')

a = exchange_to_decimal(a)
b = exchange_to_decimal(b)

# print(get_sum(a, b))
print(f'a + b = {exchange_to_hex(get_sum(a, b))}')
print(f'a + b = {"".join([str(el) for el in exchange_to_hex(get_sum(a, b))])}')

# print(get_multi(a, b))
print(f'a * b = {exchange_to_hex(get_multi(a, b))}')
print(f'a * b = {"".join([str(el) for el in exchange_to_hex(get_multi(a, b))])}')

