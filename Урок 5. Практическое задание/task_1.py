"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple, deque

QUARTERS = 4
COMPANY = namedtuple('Companies',
                     ['name_comp', 'quarters', 'profit'])
ALL_COMPANIES = set()

NUM_COMPANIES = int(input('Введите количество компаний: '))

total_profit = 0

for i in range(1, NUM_COMPANIES + 1):
    profit = 0
    quarters = []
    name_comp = input(f'Введите название {i} компании: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Введите прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = COMPANY(name_comp=name_comp,
                   quarters=tuple(quarters),
                   profit=profit)

    ALL_COMPANIES.add(comp)
    total_profit += profit

average = total_profit / NUM_COMPANIES

# 1 способ решения:
print(f'\nСредняя прибыль за год для всех преприятий = {average}')

print(f'\nКомпания, с прибылью выше среднего:')
for comp in ALL_COMPANIES:
    if comp.profit > average:
        print(f'Компания "{comp.name_comp}" заработала {comp.profit}р.')

print(f'\nКомпания, с прибылью ниже среднего:')
for comp in ALL_COMPANIES:
    if comp.profit < average:
        print(f'Компания "{comp.name_comp}" заработала {comp.profit}р.')

# 2 способ решения
sort_comanies = deque([None])
for comp in ALL_COMPANIES:
    if comp.profit > average:
        sort_comanies.append(comp)
    elif comp.profit < average:
        sort_comanies.appendleft(comp)

text = 'меньше'
for comp in sort_comanies:
    if comp is None:
        text = 'больше'
    else:
        print(f'\nКомпания {comp.name_comp} заработала {text}, чем средняя прибыль. А именно: {comp.profit}')
