# 4. Определить, какое число в массиве встречается чаще всего.
import random


# Вариант 1. С использованием словарей
def get_count1(arr):
    temp_dict = {el: arr.count(el) for el in arr}
    return {f'Число {key}': f'встречается {value} раз' for key, value in temp_dict.items() if value == max(temp_dict.values())}


# Вариант 2. Данная функция не совсем верная, т.к. возвращает только первый вариант с максимальным количесвто вхождений.
# Данная функция справедлива только для варианта с одним числом с максимальным количеством вхождений.
def get_count2(arr):
    counter = 0
    value = None
    for el in arr:
        if counter < arr.count(el):
            counter = arr.count(el)
            value = el
    return f'Число {value} встречатеся {counter} раз'


spam = [random.randint(0, 5) for _ in range(0, 30)]
print(f'Сгенерированный массив {spam}')
print('---Вариант 1---')
print(get_count1(spam))
print('---Вариант 2---')
print(get_count2(spam))
