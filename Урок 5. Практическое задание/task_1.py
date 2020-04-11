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

F = int(input('Введите количество предприятий для расчета прибыли: '))
MXM, MNM = [], []
Business = defaultdict(list)

for i in range(F):
    Business[input('Введите название предприятия: ')] = input('через пробел введите '
        'прибыль данного\n предприятия за каждый квартал(Всего 4 квартала): ').split()

for elm in Business:
    Business[elm].append(sum(int(i) for i in Business[elm]))

ecvator = sum(list(Business.get(j)[4] for j in list(i for i in Business.keys()))) / F

for elm in Business:
    if Business.get(elm)[4] < ecvator:
        MNM.append(elm)
    else:
        MXM.append(elm)

print(f'Средняя годовая прибыль всех предприятий: {ecvator}')
print(f'Предприятия, с прибылью выше среднего значения: {MXM}\n'
      f'Предприятия, с прибылью ниже среднего значения:{MNM}')

"""Не получилось реализовать с помощью namedtuple
тк p переписывается при каждом цикле, а хотелось бы создать новый экземпляр
но не знаю как в цикле сделать создание новой переменной (на пример: p1, p2, p3, и тд)

from collections import namedtuple

F = int(input('Введите количество предприятий для расчета прибыли: '))
Business = namedtuple('Business', 'name cost')

for i in range(F):
    p = Business(
        name=input('Введите название предприятия: '),
        cost=list(str(input('через пробел введите прибыль данного предприятия '
                            'за каждый квартал(Всего 4 квартала): ')).split()),
        # хотел создать еще один параметр в котором бы хранилась средняя прибыль
        # ecvator=sum(int(i) for i in p.cost) / len(p.cost) #  не получается обратить ся к p.cost из генеритора
    )
    s = sum(int(i) for i in p.cost) / len(p.cost)
    print(f'{p},\n{s}')
    print(p.cost)"""
