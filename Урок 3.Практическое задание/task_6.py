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

LIST_N = [random.randint(0, 100) for i in range(10)]

print(f"Массив: {LIST_N}")

INDEX_MIN, INDEX_MAX = 0, 0
NUMBER_MIN, NUMBER_MAX = LIST_N[INDEX_MIN], LIST_N[INDEX_MAX]

for i in range(1, len(LIST_N)):
    if LIST_N[i] < NUMBER_MIN:
        NUMBER_MIN = LIST_N[i]
        INDEX_MIN = i
    if LIST_N[i] > NUMBER_MAX:
        NUMBER_MAX = LIST_N[i]
        INDEX_MAX = i

if INDEX_MIN < INDEX_MAX:
    INDEX_START, INDEX_FINISH = INDEX_MIN, INDEX_MAX
else:
    INDEX_START, INDEX_FINISH = INDEX_MAX, INDEX_MIN

RESULT = 0

for i in range(INDEX_START + 1, INDEX_FINISH):
    RESULT += LIST_N[i]

print(f"Сумма элементов между минимальным({NUMBER_MIN}) и максимальным({NUMBER_MAX})"
      f" элементами: {RESULT}")
