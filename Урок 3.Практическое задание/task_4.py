"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию MAX_ с параметром key
"""
from random import randint


LST_LEN = 25
ARR = [randint(0, 20) for i in range(LST_LEN)]
print(ARR)

ARR_SET = set(ARR)     # Получаем только уникальные элементы

MAX = None     # Наиболее частый элемент
MAX_COUNT = 0          # Его количество

for item in ARR_SET:
    qty = ARR.count(item)
    if qty > MAX_COUNT:
        MAX_COUNT = qty
        MAX = item
        
print(f'Наиболе частый элемент: {MAX}, количество его появлений {MAX_COUNT}')


# 2-й вариант без использования set()

MAX_1 = ARR[0]
MAX_COUNT_1 = ARR.count(MAX_1)

for el in ARR:
    if ARR.count(el) > MAX_COUNT_1:
        MAX_1 = el
        MAX_COUNT_1 = ARR.count(el)
print(f'Наиболе частый элемент: {MAX_1} количество его появлений {MAX_COUNT_1}')

# 3 вариант  с использованием max()

MAX_COUNT_2 = max([(i, ARR.count(i)) for i in set(ARR)], key=lambda t: t[1])
print(MAX_COUNT_2)



# 4 вариант  с использованием sorted()

MAX_COUNT_3 = sorted([(i, ARR.count(i)) for i in set(ARR)], key=lambda t: t[1])[-1]
print(MAX_COUNT_3)

print('Могут появляться разные значения из-за того что у разных элементов частота появления может совпадать!')
