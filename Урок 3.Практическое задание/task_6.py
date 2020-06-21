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

import random

START_RANGE = 1
END_RANGE = 100
SIZE_RANGE = 10

MY_LIST = [random.randint(START_RANGE, END_RANGE) for _ in range(SIZE_RANGE)]
print(MY_LIST)

ELEM_MIN = 0
ELEM_MAX = 0

for i in range(1, len(MY_LIST)):
    if MY_LIST[i] < MY_LIST[ELEM_MIN]:
        ELEM_MIN = i
    elif MY_LIST[i] > MY_LIST[ELEM_MAX]:
        ELEM_MAX = i

if ELEM_MIN > ELEM_MAX:
    MY_LIST[ELEM_MIN], MY_LIST[ELEM_MAX] = MY_LIST[ELEM_MAX], MY_LIST[ELEM_MIN]

print(f'Левая граница: {MY_LIST[ELEM_MIN]}\n'
      f'Правая граница: {MY_LIST[ELEM_MAX]}')

SUMM = 0
for i in range(ELEM_MIN + 1, ELEM_MAX):
    SUMM += MY_LIST[i]
print(f'Сумма элементов массива = {SUMM}')
