"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""


from random import randint

my_list = [randint(0, 5) for i in range(0, 10)]
print(my_list)

print(max(my_list, key=lambda x: my_list.count(x)))
