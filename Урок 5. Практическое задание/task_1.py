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
from random import randint

# Режим отладки
# DEBUG_MODE == True - Данные вводятся автоматически
# DEBUG_MODE == False - Данные вводятся пользователем
# (проверку на правильность ввода пользователем делать не стал, посчитал для задачи излишним)
DEBUG_MODE = True
DEBUG_COMPANY_NAMES = ["IBM", "Facebook", "Google", "Yandex", "Coca Cola"]

print("Введите количество предприятий для расчета прибыли: ", end="")
if DEBUG_MODE:
    COMPANY_CNT = randint(3, 5)
    print(COMPANY_CNT)
else:
    COMPANY_CNT = int(input())

COMPANY = namedtuple('company', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

COMPANIES = []

for i in range(COMPANY_CNT):
    print(f"Введите наименование предприятия № {i+1}: ", end="")
    if DEBUG_MODE:
        COMPANY_NAME = DEBUG_COMPANY_NAMES[i]
        print(COMPANY_NAME)
    else:
        COMPANY_NAME = input()
    print("через пробел введите прибыль данного предприятия")
    print(f"за каждый квартал(Всего 4 квартала):", end="")
    if DEBUG_MODE:
        PROFIT_STR = f"{randint(100, 1000)} {randint(100, 1000)} "\
                     f"{randint(100, 1000)} {randint(100, 1000)}"
        print(PROFIT_STR)
    else:
        PROFIT_STR = input()
    PROFIT = list(map(int, PROFIT_STR.split()))
    COMPANIES.append(COMPANY(
        name=COMPANY_NAME,
        quarter_1=PROFIT[0],
        quarter_2=PROFIT[1],
        quarter_3=PROFIT[2],
        quarter_4=PROFIT[3],
        year=sum(PROFIT)
    ))

print(f"Введены следующие данные:")
for company in COMPANIES:
    print(company)

PROFIT_TOTAL = 0
for company in COMPANIES:
    PROFIT_TOTAL += company.year
PROFIT_AVG = PROFIT_TOTAL / COMPANY_CNT

print()
print(f"Средняя годовая прибыль всех предприятий: {PROFIT_AVG:.2f}")

print()
print("Предприятия, с прибылью выше среднего значения: ")
for company in COMPANIES:
    if company.year > PROFIT_AVG:
        print(f"{company.name} {company.year}")

print()
print("Предприятия, с прибылью ниже среднего значения: ")
for company in COMPANIES:
    if company.year < PROFIT_AVG:
        print(f"{company.name} {company.year}")
