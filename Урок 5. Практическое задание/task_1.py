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
from collections import defaultdict
from collections import namedtuple


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено корректно
def input_number(string):
    while True:
        try:
            number = input(f"{string}\n")
            number = int(number)
            break
        except ValueError:
            print("Не удалось преобразовать в число")
    return number


company_cnt = input_number('Введите количество предприятий')
companies = []
for i in range(company_cnt):
    company = defaultdict(lambda: None)
    company_name = input('Введите название предприятия\n')
    print('Введите прибыль данного предприятия за каждый квартал (всего 4)')
    profit = []
    for j in range(4):
        profit.append(input_number(f'Введите прибыль за {j+1} квартал: '))
    company['name'] = company_name
    company['profit'] = profit
    companies.append(company)
# Подсчет средней годовой
avg = 0
for company in companies:
    avg += sum(company['profit'])
avg /= len(companies) if len(companies) else 1
print(f'Средняя годовая прибыль всех предприятий: {avg}')
# Вывод компаний
company_names = [company["name"] for company in companies if sum(company["profit"]) >= avg]
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(company_names)}')
company_names = [company["name"] for company in companies if sum(company["profit"]) < avg]
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(company_names)}')


# То же самое, но с namedtuple
COMPANY = namedtuple('Company', 'name profit sum')
company_cnt = input_number('Введите количество предприятий')
companies = []
for i in range(company_cnt):
    company_name = input('Введите название предприятия\n')
    print('Введите прибыль данного предприятия за каждый квартал (всего 4)')
    profit = []
    for j in range(4):
        profit.append(input_number(f'Введите прибыль за {j+1} квартал: '))
    companies.append(COMPANY(company_name, profit, sum(profit)))
# Подсчет средней годовой
avg = 0
for company in companies:
    avg += company.sum
avg /= len(companies) if len(companies) else 1
print(f'Средняя годовая прибыль всех предприятий: {avg}')
# Вывод компаний
company_names = [company.name for company in companies if company.sum >= avg]
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(company_names)}')
company_names = [company.name for company in companies if company.sum < avg]
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(company_names)}')
