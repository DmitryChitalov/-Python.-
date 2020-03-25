"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
from random import random
NUMBER_LIST = int(input('Введите количество элементов в массиве: '))
BASE_LIST = []
for i in range(NUMBER_LIST):
    BASE_LIST.append(int(random() * 100))
MAX_ELEM = max(BASE_LIST)
MIN_ELEM = min(BASE_LIST)
IDX_MAX_ELEM = BASE_LIST.index(MAX_ELEM)
IDX_MIN_ELEM = BASE_LIST.index(MIN_ELEM)
if IDX_MAX_ELEM > IDX_MIN_ELEM:
    SUM_OF_ELEMS = sum(BASE_LIST[IDX_MIN_ELEM + 1:IDX_MAX_ELEM])
elif IDX_MAX_ELEM < IDX_MIN_ELEM:
    SUM_OF_ELEMS = sum(BASE_LIST[IDX_MAX_ELEM + 1:IDX_MIN_ELEM])
print(f'Массив: {BASE_LIST}')
print(f'Сумма элементов между минимальным ({MIN_ELEM}) и максимальным '
      f'({MAX_ELEM}) элементами: {SUM_OF_ELEMS}')
