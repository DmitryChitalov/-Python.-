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

COMPANY_NUMBERS = int(
    input("Введите количество предприятий для расчета прибыли: "))

COMPANY_LIST = collections.OrderedDict()

for i in range(COMPANY_NUMBERS):
    filling_out_name = input('Введите название предприятия: ')
    filling_out_profit = input(
        'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
    COMPANY_LIST[filling_out_name] = sum([int(i) for i in filling_out_profit])

AVR_PROFIT = sum(COMPANY_LIST.values()) / COMPANY_NUMBERS
print("Средняя прибыль всех предприятий " + str(round(AVR_PROFIT, 3)))
print("Компании с прибылью меньше либо равной средней: ")
for k, v in COMPANY_LIST.items():
    if v <= AVR_PROFIT:
        print(k)
print("Компании с прибылью больше средней: ")
for k, v in COMPANY_LIST.items():
    if v > AVR_PROFIT:
        print(k)
