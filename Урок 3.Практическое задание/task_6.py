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

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)

MIN_I = 0
MAX_I = 0

for i in range(1, len(EXAMPLE)):
    if EXAMPLE[i] < EXAMPLE[MIN_I]:
        MIN_I = i
    elif EXAMPLE[i] > EXAMPLE[MAX_I]:
        MAX_I = i

print(f'On index {MIN_I} is minimal element, {EXAMPLE[MIN_I]}')
print(f'On index {MAX_I} is maximal element, {EXAMPLE[MAX_I]}')

if MIN_I > MAX_I:
    MIN_I, MAX_I = MAX_I, MIN_I

SUMM = 0
for i in range(MIN_I + 1, MAX_I):
    SUMM += EXAMPLE[i]
print(SUMM)
