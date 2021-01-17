# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
import cProfile


size = 10
eggs = [random.randrange(0, 50) for _ in range(2 * size + 1)]
spam = eggs.copy()
spam1 = eggs.copy()


# Вариант 1
def median_search(arr):
    """
    Функция поиска медианы численнго ряда без его предварительной сортировки.
    Данная функция используется для ряда, где числа могут повторяться.

    Функция использует дополнительную память под 3 списка: числа меньше медианы, больше, либо равны.
    Также я завел переменную в которой хранится позиция медианы - mid_pos.

    Если ряд состоит только из уникальных чисел, то функцию можно упростить.

    Принцип поиска прост:
    а) раскидываем числа в списки по условию;
    б) объединяем списки в новый список - левый + средний + правый = новый список
    в) делаем проверку числа на равенство числу находящемуся в средней позиции нового списка,
       если число удовлетворяет условию, то это число и есть искомая медиана.

    """

    mid_pos = len(arr) // 2

    for i in range(len(arr)):
        left = []
        middle = []
        right = []

        for j in range(len(arr)):
            if arr[j] < arr[i]:
                left.append(arr[j])
            elif arr[j] == arr[i]:
                middle.append(arr[j])
            else:
                right.append(arr[j])

        temp_arr = left + middle + right
        # print(left, middle, right)
        if arr[i] == temp_arr[mid_pos]:
            return f'Медиана ряда по первому методу: {arr[i]}'


# Вариант 2
def find_smallest(arr):
    """Функция возращающая позицию минимального элемента списка."""
    smallest = arr[0]
    smallest_pos = 0
    for i, el in enumerate(arr):
        if el < smallest:
            smallest = el
            smallest_pos = i
    return smallest_pos


def find_biggest(arr):
    """Функция возращающая позицию максимального элемента списка."""
    biggest = arr[0]
    biggest_pos = 0
    for i, el in enumerate(arr):
        if el > biggest:
            biggest = el
            biggest_pos = i
    return biggest_pos


def median_search2(arr):
    """
    В данной функции за одну итерацию происходит поиск и удаление минимального и максимального занчений ряда.
    Функция возвращает, то что осталось после окончания цикла. А, именно, средний элемент.
    Фактически это сортировка выбором.
    """
    half_len = len(arr) // 2
    for i in range(half_len):
        arr.pop(find_smallest(arr))
        arr.pop(find_biggest(arr))
    return f'Медиана ряда по второму методу: {arr[0]}'


print(f'Исходный список: {eggs}')
print(f'Отсортированны список: {list(sorted(eggs))}')
print(median_search(spam))
print(median_search2(spam1))

