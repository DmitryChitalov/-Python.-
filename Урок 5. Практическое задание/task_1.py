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

# первый вариант с использованием ChainMap
from collections import ChainMap
from functools import reduce

N = int(input('Введите количество предприятий для расчета прибыли: '))
COUNT = 0
COMPANY_DATA = ChainMap()

while COUNT != N:
    COUNT += 1
    NAME = input('Введите название предприятия: ')
    COMPANY_PROFIT = input('через пробел введите прибыль данного'
                             'предприятия за каждый квартал(Всего 4 квартала):').split()
    # считаем среднию прибыль предприятия
    AVG = reduce(lambda x, y: int(x) + int(y), COMPANY_PROFIT)
    # заполняем цепочку словарей
    COMPANY_DATA.update({NAME: AVG})
# считаем среднию прибыль всех предприятий
AVG_PROFIT_ALL = sum(COMPANY_DATA.values())/N

HIGH_AVG = []
LOW_AVG = []

for key in COMPANY_DATA.keys():
    if COMPANY_DATA.get(key) > AVG_PROFIT_ALL:
        HIGH_AVG.append(key)
    elif COMPANY_DATA.get(key) < AVG_PROFIT_ALL:
        LOW_AVG.append(key)


print(f'Средняя годовая прибыль всех предприятий: {AVG_PROFIT_ALL}')
print(f'Предприятия, с прибылью выше среднего значения: {" ".join(HIGH_AVG)}')
print(f'Предприятия, с прибылью меньше среднего значения: {" ".join(LOW_AVG)}')




# второй вариант реализации с использованием namedtuple

from collections import namedtuple

N = int(input('Введите количество предприятий для расчета прибыли: '))
COUNT = 0

# объявляем кортеж
CompanyData = namedtuple('COMAPINIES_DATA', 'first second third firth')

# создаем словарь для хранения кортежей
COMPANY_ALL = {}

while COUNT != N:
    COUNT += 1
    NAME = input('Введите название предприятия: ')
    COMPANY_PROFIT = input('через пробел введите прибыль данного'
                             'предприятия за каждый квартал(Всего 4 квартала):').split()

    # заполняем кортеж данными за каждый квартал
    # на случай если понадобиться вытащить данные за каждый
    # квартал по конкретному предприятию

    COMPANY_ALL[NAME] = CompanyData(
        first=int(COMPANY_PROFIT[0]),
        second=int(COMPANY_PROFIT[1]),
        third=int(COMPANY_PROFIT[2]),
        firth=int(COMPANY_PROFIT[3])
    )
# считаем общию прибыль
TOTAL_PROFIT = 0

for name, profit in COMPANY_ALL.items():
    TOTAL_PROFIT += sum(profit)

# считаем среднию прибыль
AVG_ALL = TOTAL_PROFIT / N

HIGH_AVG = []
LOW_AVG = []

for name, profit in COMPANY_ALL.items():
    if sum(profit) > AVG_ALL:
        HIGH_AVG.append(name)
    elif sum(profit) < AVG_ALL:
        LOW_AVG.append(name)

print(f'Средняя годовая прибыль всех предприятий: {AVG_ALL}')
print(f'Предприятия, с прибылью выше среднего значения: {" ".join(HIGH_AVG)}')
print(f'Предприятия, с прибылью меньше среднего значения: {" ".join(LOW_AVG)}')
