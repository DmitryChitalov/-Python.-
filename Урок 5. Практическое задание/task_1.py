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

def profit():
    n = int(input("Введите количество предприятий: "))
    companies = namedtuple("Company", "name quarter_1 quarter_2 quarter_3 quarter_4")
    profit_annual = {}
    for i in range(n):
        company = companies(name=input("Введите название компании: "),
                            quarter_1=int(input("Введите прибыль за первый квартал: ")),
                            quarter_2=int(input("Введите прибыль за второй квартал: ")),
                            quarter_3=int(input("Введите прибыль за третий квартал: ")),
                            quarter_4=int(input("Введите прибыль за четвертый квартал: ")))
        profit_annual[company.name] = \
            company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4

    total_annual = 0
    for value in profit_annual.values():
        total_annual += value
    total_annual = total_annual / n
    print(f"Средняя годовая прибыль предприятий - {total_annual}")

    for key, value in profit_annual.items():
        if value > total_annual:
            print(f"Предприятия с прибылью выше среднего: {key}")
        elif value < total_annual:
            print(f"Предприятия с прибылью ниже среднего: {key}")


profit()