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


class CompanyCounter:

    def __init__(self):
        self.companies = collections.defaultdict(list)
        self.company = collections.namedtuple('Company', ["name", "incm_1", "incm_2", "incm_3", "incm_4"])
        self.avr_income = None

    def get_average_income(self):
        total_sum = 0
        for company in self.companies.values():
            company_sum = sum(company[1:4])
            total_sum += company_sum
        total_avr = round(total_sum / len(self.companies), 2)
        self.avr_income = total_avr
        return total_avr

    def get_lower_companies(self):
        lower_cmp = list()
        for company in self.companies.values():
            company_income = sum(company[1:4])
            if company_income < self.avr_income:
                lower_cmp.append(company.name)
        return ", ".join(lower_cmp)

    def get_higher_companies(self):
        higher_cmp = list()
        for company in self.companies.values():
            company_income = sum(company[1:4])
            if company_income >= self.avr_income:
                higher_cmp.append(company.name)
        return ", ".join(higher_cmp)

    def create_company(self, name, income):
        company_obj = self.company(name, *[income.popleft() for _ in range(4)])
        self.companies[name] = company_obj


def main():
    try:
        cmp_counter = CompanyCounter()
        companies_num = int(input("Введите количество предприятий для расчета прибыли: "))
        for company in range(companies_num):
            name = input("Введите название предприятия: ")
            income = collections.deque(map(int, input("через пробел введите прибыль данного предприятия/"
                                                      " за каждый квартал(Всего 4 квартала): ").split()), maxlen=4)

            cmp_counter.create_company(name, income)
        average_income = cmp_counter.get_average_income()
        print(f"Средняя годовая прибыль всех предприятий: {average_income}")
        higher_companies = cmp_counter.get_higher_companies()
        print(f"Предприятия, с прибылью выше среднего значения: {higher_companies}")
        lower_companies = cmp_counter.get_lower_companies()
        print(f"Предприятия, с прибылью ниже среднего значения: {lower_companies}")

    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()

# OutPut:

# Введите количество предприятий для расчета прибыли: 2
# Введите название предприятия: Рога
# через пробел введите прибыль данного предприятия/ за каждый квартал(Всего 4 квартала): 235 345634 55 235
# Введите название предприятия: Копыта
# через пробел введите прибыль данного предприятия/ за каждый квартал(Всего 4 квартала): 345 34 543 34
# Средняя годовая прибыль всех предприятий: 173423.0
# Предприятия, с прибылью выше среднего значения: Рога
# Предприятия, с прибылью ниже среднего значения: Копыта


