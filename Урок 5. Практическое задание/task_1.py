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
# Вариант без модуля collections
N = int(input('Введите количество предприятий для расчета прибыли: '))
n = 1
COMPANYS = {}
SUM_PROFIT = 0
while n <= N:
    NAME = input('Введите название предприятия: ')
    PROFIT = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    PROFIT_LIST = PROFIT.split(' ')
    PROFIT_YEAR = 0
    for i in PROFIT_LIST:
        PROFIT_YEAR += int(i)
    COMPANYS[NAME] = PROFIT_YEAR
    SUM_PROFIT += PROFIT_YEAR
    n += 1

AVRG = SUM_PROFIT / N
print(f'Средняя годовая прибыль всех предприятий: {AVRG}')
for i in COMPANYS:
    if COMPANYS[i] >= AVRG:
        print(f'Предприятия, с прибылью выше среднего значения: {i}')
    else:
        print(f'Предприятия, с прибылью ниже среднего значения: {i}')

# Вариант с counter
from collections import Counter

N = int(input('Введите количество предприятий для расчета прибыли: '))
n = 1
COMPANYS = Counter()
while n <= N:
    NAME = input('Введите название предприятия: ')
    PROFIT = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    PROFIT_LIST = PROFIT.split(' ')
    for i in PROFIT_LIST:
        COMPANYS[NAME] += int(i)
    n += 1

SUM_COMP = 0
for j in COMPANYS:
    SUM_COMP += COMPANYS[j]
AVRG = SUM_COMP / N
print(f'Средняя годовая прибыль всех предприятий: {AVRG}')
for i in COMPANYS:
    if COMPANYS[i] >= AVRG:
        print(f'Предприятия, с прибылью выше среднего значения: {i}')
    else:
        print(f'Предприятия, с прибылью ниже среднего значения: {i}')

# Вариант с namedtuple (этот вариант получится корявый, тк я не придумала, как сделать с циклом)
from collections import namedtuple

COMPANY = namedtuple('COMPANY', 'name profit')
COMPANY_1 = COMPANY(name='OOO_ONE', profit='741212 3258 741221 3698')
COMPANY_2 = COMPANY(name='OOO_TWO', profit='985211 1478 2222 3652')
COMPANY_3 = COMPANY(name='OOO_THREE', profit='2147851 7854 9632 1211')

PROFIT_1 = 0
PROFIT_2 = 0
PROFIT_3 = 0
for i in COMPANY_1.profit.split(' '):
    PROFIT_1 += int(i)
for i in COMPANY_2.profit.split(' '):
    PROFIT_2 += int(i)
for i in COMPANY_3.profit.split(' '):
    PROFIT_3 += int(i)
print(PROFIT_1, PROFIT_2, PROFIT_3)
AVRG = (PROFIT_1 + PROFIT_2 + PROFIT_3) / 3
print(f'Средняя годовая прибыль всех предприятий: {int(AVRG)}')
if PROFIT_1 > AVRG:
    print(f'{COMPANY_1.name} - прибыль выше среднего значения.')
else:
    print(f'{COMPANY_1.name} - прибыль ниже среднего значения.')

if PROFIT_2 > AVRG:
    print(f'{COMPANY_2.name} - прибыль выше среднего значения.')
else:
    print(f'{COMPANY_2.name} - прибыль ниже среднего значения.')

if PROFIT_3 > AVRG:
    print(f'{COMPANY_3.name} - прибыль выше среднего значения.')
else:
    print(f'{COMPANY_3.name} - прибыль ниже среднего значения.')