from collections import namedtuple

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
n = int(input('Enter number of companies: '))
PROF = namedtuple('Profit', 'name year_prof')
all_copm = [0] * n
total = 0
for i in range(n):
    all_copm[i] = PROF(
        name=input('Enter company name: '),
        year_prof=sum(tuple(map(int, input('Enter company profit for each quarter: ').split())))
    )
    total += all_copm[i].year_prof
average_prof = total / n
print(f'Average profit of all companies: {average_prof}')
more_avg = [i.name for i in all_copm if i.year_prof > average_prof]
less_avg = [i.name for i in all_copm if i.year_prof < average_prof]
print('Companies with profit more than average:')
print(*more_avg)
print('Companies with profit less than average:')
print(*less_avg)
