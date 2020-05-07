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


from collections import namedtuple


Corporation = namedtuple(
    'Corporation', 'name quarter_1 quarter_2 quarter_3 quarter_4 total')

corp_count = int(input('Введите количество предприятий для расчета: '))
corporations = [0 for _ in range(corp_count)]
profit_sum = 0

for i in range(corp_count):
    name = input(f'Введите название {i+1}-го предприятия: ')
    quarters = [float(prof) for prof in input(
        'Введите через пробел прибыль в каждом квартале: ').split()]

    total = 0
    for quarter in quarters:
        total += quarter

    profit_sum += total
    corporations[i] = Corporation(name, *quarters, total)

if corp_count > 1:
    profit_average = profit_sum / corp_count

    less = []
    more = []

    for i in range(corp_count):

        if corporations[i].total < profit_average:
            less.append(corporations[i])

        elif corporations[i].total > profit_average:
            more.append(corporations[i])

    print(f'\nСредняя годовая прибыль всех предприятий: {profit_average: .2f}')

    print(
        f'Предприятия, с прибылью ниже среднего значения {profit_average: .2f}:')
    for ent in less:
        print(f'Предприятие "{ent.name}" с прибылью {ent.total: .2f}')

    print(
        f'\nПредприятия, с прибылью выше среднего значения {profit_average: .2f}:')
    for ent in more:
        print(f'Предприятие "{ent.name}" с прибылью {ent.total: .2f}')
else:
    print(
        f'Предприятие: {enterprises[0].name}. Годовая прибыль: {corporations[0].year}')
