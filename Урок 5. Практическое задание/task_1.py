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

a = int(input('Введите количество предприятий для расчета прибыли: '))
corp = namedtuple('Corp_case', 'name_corp one_qua two_qua three_qua four_qua')
data_base = {}
for i in range(a):
    stat_corp = corp(name_corp=input('Введите название предприятия: '),
                     one_qua=int(input('Введите прибыль за 1 квартал: ')),
                     two_qua=int(input('Введите прибыль за 2 квартал: ')),
                     three_qua=int(input('Введите прибыль за 3 квартал: ')),
                     four_qua=int(input('Введите прибыль за 4 квартал: ')))
    data_base[stat_corp.name_corp] = (stat_corp.one_qua + stat_corp.two_qua
                                      + stat_corp.three_qua + stat_corp.four_qua) / 4
print(data_base)
average_profit = 0
for i in data_base.values():
    average_profit += i
average_profit /= a
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
for x, y in data_base.items():
    if y > average_profit:
        print(f'Предприятие {x} имеет прибыль выше среднего')
    else:
        print(f'Предприятие {x} имеет прибыль ниже среднего')
# Второй вариант
a = int(input('Введите количество предприятий для расчета прибыли: '))
corp = deque()
data_base = {}
for i in range(a):
    corp = []
    x = 0
    names = input('Введите название предприятия: ')
    corp.append(int(input('Введите прибыль за 1 квартал: ')))
    corp.append(int(input('Введите прибыль за 2 квартал: ')))
    corp.append(int(input('Введите прибыль за 3 квартал: ')))
    corp.append(int(input('Введите прибыль за 4 квартал: ')))
    print(corp)
    for j in corp:
        x += j
    data_base[names] = x
print(data_base)
average_profit = 0
for i in data_base.values():
    average_profit += i
average_profit /= a
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
for x, y in data_base.items():
    if y > average_profit:
        print(f'Предприятие {x} имеет прибыль выше среднего')
    else:
        print(f'Предприятие {x} имеет прибыль ниже среднего')
