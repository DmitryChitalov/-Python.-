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

company = collections.namedtuple('company', ['q1', 'q2', 'q3', 'q4', 'ye'])

companies = {}

n = int(input("Enter number of companies: "))

for i in range(n):
    name = input(f"Name of {i + 1} company: ")
    profit_q1 = int(input('Profit of the 1 quarter: '))
    profit_q2 = int(input('Profit of the 2 quarter: '))
    profit_q3 = int(input('Profit of the 3 quarter: '))
    profit_q4 = int(input('Profit of the 4 quarter: '))
    companies[name] = company(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4,
        ye=profit_q1 + profit_q2 + profit_q3 + profit_q4)

total_profit = 0

for name in companies.keys():
    total_profit += companies[name].ye

result_above = [x for x in companies.keys() if companies[x].ye > (total_profit / n)]
result_below = [x for x in companies.keys() if companies[x].ye <= (total_profit / n)]

print(f"Companies with year profit more than average: {', '.join(result_above)}")
print(f"Companies with year profit less than average: {', '.join(result_below)}")
