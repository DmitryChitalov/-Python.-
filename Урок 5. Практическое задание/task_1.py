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

from functools import reduce
import collections

Organization = collections.namedtuple('Organization', ['name', 'qrtr_1', 'qrtr_2', 'qrtr_3', 'qrtr_4'])
ORG = []

# ORG = [Organization("Рога", 235, 345634, 55, 235), Organization("Копыта", 345, 34, 543, 34)]
try:
    AMOUNT_ORG = int(input('Введите количество предприятий для расчета прибыли: '))
except ValueError:
    print("Ошибка: Вы ввели не число!")
    AMOUNT_ORG = 1

while AMOUNT_ORG:
    name = input('Введите название предприятия: ')
    quarts = map(int, input(
        'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split())
    try:
        ORG.append(Organization(name, *quarts))
    except TypeError:
        print('Ошибка: введено не 4 значения прибыли!')
        continue
    AMOUNT_ORG -= 1

COMP_YEAR_GAIN = {}
for elem in ORG:
    year_average = (elem.qrtr_1 + elem.qrtr_2 + elem.qrtr_3 + elem.qrtr_4) / 4
    # year_average = (sum(elem[1:4])) / 4  # решил не использовать данный способ в целях обучения
    COMP_YEAR_GAIN.setdefault(elem.name, year_average)

TOTAL_YEAR_GAIN = reduce(lambda a, b: a + b, (elem for elem in COMP_YEAR_GAIN.values())) / len(COMP_YEAR_GAIN)
print(f'Средняя годовая прибыль всех предприятий: {TOTAL_YEAR_GAIN}')
print(f'Предприятия, с прибылью выше среднего значения: '
      f'{" ".join(name for name, val in COMP_YEAR_GAIN.items() if val > TOTAL_YEAR_GAIN)}')
print(f'Предприятия, с прибылью ниже среднего значения: '
      f'{" ".join(name for name, val in COMP_YEAR_GAIN.items() if val < TOTAL_YEAR_GAIN)}')
