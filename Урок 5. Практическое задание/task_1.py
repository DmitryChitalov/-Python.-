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
# ВАРИАНТ 1
from collections import defaultdict

n = int(input("Введите количество предприятий для расчета прибыли: "))

FIRMS = defaultdict()
for i in range(n):
    NAME = input(f"Введите название {i+1}-го предприятия: ")
    PROFITS = list(map(int, input(f"Через пробел введите прибыль {i+1}-го предприятия "\
                         "за каждый квартал(Всего 4 квартала): ").split(" ")))
    FIRMS[NAME] = PROFITS
print(FIRMS)

TTL_PROFITS = 0
for key in FIRMS:
    TTL_PROFITS += sum(FIRMS.get(key))

AVER_PROFITS = round(TTL_PROFITS / n, 2)

LESS = []
MORE = []
for key in FIRMS:
    if (sum(FIRMS.get(key))) < AVER_PROFITS:
        LESS.append(key)
    elif (sum(FIRMS.get(key))) > AVER_PROFITS:
        MORE.append(key)
LESS = ", ".join(LESS)
MORE = ", ".join(MORE)

print(f"Средняя годовая прибыль всех предприятий: {AVER_PROFITS}")
print(f"Предприятия, с прибылью выше среднего значения: {MORE}")
print(f"Предприятия, с прибылью ниже среднего значения: {LESS}")


# ВАРИАНТ 2
from collections import namedtuple

n = int(input("Введите количество предприятий для расчета прибыли: "))

FIRMS = namedtuple(
    "FIRM",
    "NAME QUARTER_1 QUARTER_2 QUARTER_3 QUARTER_4"
)
YEAR_PROFITS = {}

for i in range(n):
    NAME = input(f"Введите название {i + 1}-го предприятия: ")
    PROFITS = list(map(int, input(f"Через пробел введите прибыль {i+1}-го предприятия "\
                         "за каждый квартал(Всего 4 квартала): ").split(" ")))
    FIRM = FIRMS(
        NAME=NAME,
        QUARTER_1=PROFITS[0],
        QUARTER_2=PROFITS[1],
        QUARTER_3=PROFITS[2],
        QUARTER_4=PROFITS[3]
    )
    YEAR_PROFITS[FIRM.NAME] = FIRM.QUARTER_1 + FIRM.QUARTER_2 + FIRM.QUARTER_3 + FIRM.QUARTER_4

TTL_PROFITS = 0
for value in YEAR_PROFITS.values():
    TTL_PROFITS += value

AVER_PROFITS = round(TTL_PROFITS / n, 2)

LESS = []
MORE = []
for key, value in YEAR_PROFITS.items():
    if value < AVER_PROFITS:
        LESS.append(key)
    elif value > AVER_PROFITS:
        MORE.append(key)
LESS = ", ".join(LESS)
MORE = ", ".join(MORE)

print(f"Средняя годовая прибыль всех предприятий: {AVER_PROFITS}")
print(f"Предприятия, с прибылью выше среднего значения: {MORE}")
print(f"Предприятия, с прибылью ниже среднего значения: {LESS}")
