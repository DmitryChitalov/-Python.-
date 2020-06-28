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

Company = namedtuple('Company', 'name first second third fourth')
list_companies = []
total_income = 0

comp_number = int(input('How many companies?: '))
for i in range(1, comp_number + 1):
    counter = comp_number
    comp_name = input(f'Enter a name of {i} company: ')
    comp_income = (input(f'Enter income for each quarter for {i} company: ').split())
    Company = namedtuple('Company', 'name first second third fourth')
    Comp = Company(
        name=comp_name,
        first=comp_income[0],
        second=comp_income[1],
        third=comp_income[2],
        fourth=comp_income[3]
    )
    list_companies.append(Comp)
    counter -= 1

# В цикле определяем какая из компаний имеет макисмльную прибыль и определяем среднюю прибыль для всех компаний за год
for j in list_companies:
    comp_income = int(j.first) + int(j.second) + int(j.third) + int(j.fourth)
    total_income += comp_income
average_profit = (total_income / comp_number)
print(f"The total income of {comp_number} companies is {total_income} ")
print(f"The average profit for a year for {comp_number} companies is {average_profit} ")

# В цикле опредялем какая из компаний имеет выше или ниже среднегодовой доход чем среднегодовой доход по всем компаниям
for x in list_companies:
    if (int(x.first) + int(x.second) + int(x.third) + int(x.fourth)) > average_profit:
        print(
            f"The '{x.name}' company has higher income than the average profit for all companies, "
            f"which is {average_profit}")
    elif (int(x.first) + int(x.second) + int(x.third) + int(x.fourth)) < average_profit:
        print(
            f"The '{x.name}' company has lower income than the average profit for all companies, "
            f"which is {average_profit}")
    elif (int(x.first) + int(x.second) + int(x.third) + int(x.fourth)) == average_profit:
        print(f"The '{x.name}' company has the average profit, which is {average_profit}")
    else:
        print(
            f'Looks like there are something wrong in entered data. Please, check it again')
