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

MyProfit = collections.namedtuple('MyProfit', 'I, II, III, IV, profit')
MyFirm = collections.namedtuple('MyFirm', 'name, profit')

firms_collection = []

firms_count = int(input('Введите количество компаний: '))
for i in range(firms_count):
    a_name = input('Введите название компании: ')
    is_repeat = True
    a_profit_list = []
    while is_repeat or len(a_profit_list) < 4:
        try:
            a_profit = input('Введите поквартальную прибыль за год через пробел: ')
            a_profit_list = tuple(map(float, a_profit.split()[:4]))
            is_repeat = False
        except ValueError as err:
            print(err, 'Повторите ввод...')
            is_repeat = True
    tmp = MyProfit(*a_profit_list[:4], sum(a_profit_list))
    firms_collection.append(MyFirm(a_name, tmp))

avg_sum = sum([i.profit.profit for i in firms_collection])/len(firms_collection)
print(f'\nСредняя годовая прибыль всех предприятий: {avg_sum}')
print(f'Предприятия, с прибылью выше среднего значения: {[i.name for i in firms_collection if i.profit.profit > avg_sum]}')
print(f'Предприятия, с прибылью ниже среднего значения: {[i.name for i in firms_collection if i.profit.profit < avg_sum]}')
