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
from random import randint

COUNT = int(input('Введите количество элементов списка: '))
LIST = [randint(0, 100) for i in range(COUNT)]
print(LIST)
MIN_VAL_IND = LIST.index(min(LIST))
MAX_VAL_IND = LIST.index(max(LIST))
if MIN_VAL_IND > MAX_VAL_IND:
    MIN_VAL_IND, MAX_VAL_IND = MAX_VAL_IND, MIN_VAL_IND

print(sum(LIST[MIN_VAL_IND+1:MAX_VAL_IND]))
