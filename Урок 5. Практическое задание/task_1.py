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

ENTERPRISE = collections.namedtuple('Enterprise', ['name', 'q1', 'q2', 'q3', 'q4'])


def input_enterprise():
    """Ввод данных с клавиатуры"""
    iname = input('Введите название предприятия: ')
    iq1 = int(input('Введите прибыль за 1 квартал: '))
    iq2 = int(input('Введите прибыль за 2 квартал: '))
    iq3 = int(input('Введите прибыль за 3 квартал: '))
    iq4 = int(input('Введите прибыль за 4 квартал: '))

    exn = ENTERPRISE(name=iname, q1=iq1, q2=iq2, q3=iq3, q4=iq4)
    return exn

def annual_revenue(exn: ENTERPRISE):
    """Total"""
    return exn.q1 + exn.q2 + exn.q3 + exn.q4

def calculate(es_new: list):
    """Расчет выше стреднего и ниже среднего занчения"""
    sum_revenue = 0
    for e_new in es_new:
        sum_revenue += annual_revenue(e_new)
    average_revenue = sum_revenue / len(es_new)

    below_avarage = list()
    above_avarage = list()

    for e_new in es_new:
        if annual_revenue(e_new) > average_revenue:
            above_avarage.append(e_new)
        elif annual_revenue(e_new) < average_revenue:
            below_avarage.append(e_new)

    return below_avarage, above_avarage

def solution():
    """Решение задачи"""
    count = int(input('Введите количество предприятий для расчета: '))
    es_new = list()

    for _ in range(count):
        e_new = input_enterprise()
        es_new.append(e_new)

    above_average, below_average = calculate(es_new)

    print("Выше среднего")
    for e_new in above_average:
        print(e_new.name)

    print("Ниже среднего")
    for e_new in below_average:
        print(e_new.name)

def test():
    """test"""
    e1_new = ENTERPRISE(name="one", q1=1, q2=1, q3=1, q4=1)
    e2_new = ENTERPRISE(name="two", q1=2, q2=2, q3=2, q4=2)
    e3_new = ENTERPRISE(name="three", q1=3, q2=3, q3=3, q4=3)

    above, below = calculate(list([e1_new, e2_new, e3_new]))

    assert len(above) == 1
    assert len(below) == 1

    print("Выше среднего", above)

    print("Ниже среднего", below)

# start
#solution()
test()
