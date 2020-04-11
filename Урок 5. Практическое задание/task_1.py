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
import collections
from functools import reduce
count_companies = int(input('Введите кол-во компаний: '))

companies = []

for i in range(count_companies):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Квартальные прибыли через пробел: ').split(' '))
    company = {
        'title': title,
        'profit_q1': profit_q1,
        'profit_q2': profit_q2,
        'profit_q3': profit_q3,
        'profit_q4': profit_q4,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    companies.append(company)

profit_col = collections.Counter()
for company in companies:
    profit_comp = company.copy()
    del profit_comp['title']
    profit_col += collections.Counter(profit_comp)

print()
for company in companies:
    print(company)

average_profit = profit_col['profit_year'] / len(companies)

print('Суммарная прибыль компаний: ', profit_col)
print('Средняя годовая прибыль компаний: ', average_profit)
print('Прибыль выше среднего: ', [x['title'] for x in companies if x['profit_year'] >= average_profit])
print('Прибыль ниже среднего: ', [x['title'] for x in companies if x['profit_year'] < average_profit])