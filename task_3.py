"""
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

# 1
dict_profit = {}
dict_company = {'Yarl' : 3460, 'Quark' : 4000, 'Cityland' : 2690, 'Ion': 1000, 'Drink': 8000, 'Drank' : 34000, 'Cross' : 4500}
values = sorted(dict_company.values())[-4 : -1]
for el in dict_company.items():
    for val in values:
        if el[1] == val:
           dict_profit.update({el})  
print(dict_profit)


# 2
dict_profit = {}
dict_company = {'Yarl' : 3460, 'Quark' : 4000, 'Cityland' : 2690, 'Ion': 1000, 'Drink': 8000, 'Drank' : 34000, 'Cross' : 4500}
values = sorted(dict_company.values())[-4 : -1]
[dict_profit.update({el}) for el in dict_company.items() for val in values if el[1] == val]
print(dict_profit)
