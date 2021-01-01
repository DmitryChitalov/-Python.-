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


# Рога 235 345634 55 235
# Копыта 345 34 543 34

# Я использовал OrderedDict, правда не понимаю зачем здесь нужен любой объект из класса collections 
from collections import OrderedDict as odict
import numpy as np

firm_profits = []
firm_info = []
num_firms = int(input('Plese provide number of rows: ').rstrip().lstrip())
i = 0
while i < num_firms:
    dic = odict()
    firm_name = str(input('Plese provide the name of firm: ').rstrip().lstrip())
    firm_profits = np.array((input('Plese provide the firm''s quarter profits separeted by spaces: ').rstrip().lstrip()).split(' '), dtype=int)
    y_profit = np.sum(firm_profits) # Посчитать суммарный годовой доход
    firm_profits = np.append(firm_profits, y_profit) # Добавит суммарный годовой доход в массив 5-ым элементом
    dic.update({firm_name : firm_profits})
    firm_info.append(dic)
    i += 1

def sum_avg():
    profit = 0
    for firm in firm_info:
        for item in firm.items():
            profit += item[1][4]
    return profit / num_firms        

all_avg = sum_avg()
for firm in firm_info:
    for item in firm.items():
        if item[1][4] > all_avg:
            print (f'Firm {item[0]} has average profit {item[1][4]} that is more than {all_avg}')
        elif item[1][4] == all_avg:
            print (f'Firm {item[0]} has average profit {item[1][4]} that is the same as {all_avg}')
        else:
            print (f'Firm {item[0]} has average profit {item[1][4]} that is less than {all_avg}')


"""
Plese provide number of rows: 2
Plese provide the name of firm: Рога
Plese provide the firms quarter profits separeted by spaces: 235 345634 55 235
Plese provide the name of firm: Копыта
Plese provide the firms quarter profits separeted by spaces: 345 34 543 34
Firm Рога has average profit 346159 that is more than 173557.5
Firm Копыта has average profit 956 that is less than 173557.5
"""






