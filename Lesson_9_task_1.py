# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib)
# задача считается не решённой.
import hashlib
from collections import Counter
import cProfile


"""Вариант №1. Без использования библиотеки hashlib."""


def get_count1(s: str):
    """
    По условиям задачи, функция принимает на вход строку состоящую только из строчных латинских букв.
    Данная функция производит хеш среза переданной строки и записывает его в словарь counter().
    """

    len_s = len(s)
    letter = 26
    spam = set()
    result = Counter()

    assert len_s > 0, 'String cannot be empty!'

    for i in range(len_s):

        """Первый цикл будет сдвигать начало среза вправо."""

        for j in range(1, len_s):

            """
            Во втором цикле получаем подстроку (среза строки).
            И проверяем ее на уникальность.
            Можно не делать проверку на уникальность, функция при этом будет работать значительно медленнее.
            """

            index = 0
            subs = s[i: i + j]

            if subs not in spam:
                spam.add(subs)

                for k, char in enumerate(subs):

                    """В третьем цикле хешируем подстроку, и записываем в result по окончании цикла."""

                    index += (ord(char) - 96) * (letter ** k)

                result[index] += 1

    return result


"""Вариант №2. С использованием библиотеки hashlib."""


def get_count2(s: str):
    """
    Данная функция производит срез переданной строки и записывает его в словарь counter().
    Если не нужно считать количество каждой уникальной строки, то вместо counter() можно использовать set().
    """
    len_s = len(s)
    result = Counter()

    assert len_s > 0, 'String cannot be empty!'

    for i in range(len_s):

        """Первый цикл будет сдвигать начало среза вправо."""

        for j in range(1, len_s):

            """
            Во втором цикле получаем хеш подстроки (среза строки).
            И записываем его в counter() с одновременным подсчетом.
            """
            h_subs = hashlib.sha1(s[i: i + j].encode('utf-8')).hexdigest()
            result[h_subs] += 1

            """
            Если раскомментировать if, то будет выполняться проверка на уникальность.
            В таком случае функция будет работать немного быстрее.
            Но, как я писал выше, лучше тогда использовать множество.
            """

            # if h_subs not in result:
            #     result[h_subs] += 1

    return result


# string = input('Enter the string: ')
# string = 'abcdefghijklmnopqrstuvwxyz'
string = 'abcdef'

# Раскомментировать ниже что бы просмотреть словарь подстрок.
print(*get_count1(string).items(), sep='\n')
print(*get_count2(string).items(), sep='\n')

print('-' * 30)

print(f'Method One: The number of unique substrings will be {len(get_count1(string))} pcs')
print(f'Method Two: The number of unique substrings will be {len(get_count2(string))} pcs')

print('-' * 30)

cProfile.run('get_count1(string)')
cProfile.run('get_count2(string)')
