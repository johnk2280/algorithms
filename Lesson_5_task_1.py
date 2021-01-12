# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import deque


def get_profit(dict_company):
    """Функция подсчета средней прибыли."""

    """
    Создаем очередь deque(), 
    которая будет выводить список компаний и среднее значение прибыли по всем компаниям.
    """

    spam = deque()
    average_profit = {key: sum(dict_company[key]) / 4 for key in dict_company.keys()}
    all_average_profit = round(sum(list(average_profit.values())) / len(average_profit), 2)

    """Добавляем среднюю прибыль по всем компаниям в очередь."""

    spam.append(all_average_profit)

    """
    Проверяем среднюю прибыль каждой компании.
    Если средняя прибыль компании меньше средней прибыли по всем компаниям,
    то добавляем наименование компании в очередь слева от значения средней прибыли,
    если больше - справа.
    """
    for key in average_profit.keys():
        if average_profit[key] >= all_average_profit:
            spam.append(key)
        else:
            spam.appendleft(key)
    return f'Companies average profit {average_profit}\n' \
           f'Average profit {all_average_profit}\n' \
           f'List of companies {list(spam)}'


"""Запрос количества компаний"""

while True:
    try:
        quantity = int(input('Enter the number of companies: '))
    except ValueError:
        print('Invalid value')
        continue
    else:
        break

"""Заправшиваем квартальную прибыль."""
k = 0
companies = {}
while k < quantity:
    quarterly_profit = []
    name_company = input(f'Enter the name of the {k + 1} company: ')
    for i in range(1, 5):
        q_p = float(input(f'Enter your profit for the {i} quarter: '))
        quarterly_profit.append(q_p)
    companies[name_company] = quarterly_profit
    k += 1

print('-' * 30)
print(companies)
print(get_profit(companies))

