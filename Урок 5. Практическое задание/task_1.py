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


import sys
from collections import defaultdict, namedtuple


def avg(iterable) -> float:
    """ Вычисление среднего значения """
    return sum(iterable) / len(iterable)


def print_result(result) -> None:
    """ Печать результатов высислений """
    print('Средняя годовая прибыль всех предприятий: ', result.general_avg)
    print('Предприятия, с прибылью выше среднего значения: ',
          ', '.join(result.companies_positive))
    print('Предприятия, с прибылью ниже среднего значения: ',
          ', '.join(result.companies_negative))


def solution(companies_number: int):
    """ Решение, используюшее defaultdict  и namedtuple одновременно """
    companies_dict = defaultdict(float)
    for _ in range(companies_number):
        company_name = input('Введите название предприятия: ').strip()
        profit = input('Введите прибыль данного предприятия за каждый'
                       ' квартал через пробел (Всего 4 квартала): ').strip()
        profit = profit.split(' ')
        try:
            profit = [float(x) for x in profit]
        except ValueError:
            print('Неверное зачение прибыли, выходим.')
            sys.exit()

        company_avg = avg(profit)
        companies_dict[company_name] = company_avg

    Result = namedtuple('Result', ['general_avg', 'companies_positive', 'companies_negative'])
    result = Result(general_avg=avg(companies_dict.values()),
                    companies_positive=[], companies_negative=[])

    for key, value in companies_dict.items():
        if value >= result.general_avg:
            result.companies_positive.append(key)
        else:
            result.companies_negative.append(key)

    return result


if __name__ == "__main__":

    try:
        CORP_NUMBER = int(
            input('Введите количество предприятий для расчета прибыли: ').strip())
    except ValueError:
        print('Неверное количество, выходим.')
        sys.exit()

    print_result(solution(CORP_NUMBER))
