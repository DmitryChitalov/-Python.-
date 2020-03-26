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

FROM, TO = 0, 100

try:
    QUANTITY = int(input('Введите количество элементов в массиве: '))
    LST = [randint(FROM, TO) for i in range(QUANTITY)]
    print(f'Массив: {LST}')
    MAX, MIN = max(LST), min(LST)
    MAX_INDEX, MIN_INDEX = LST.index(MAX), LST.index(MIN)
    SUMM = sum(LST[MIN_INDEX + 1: MAX_INDEX]
               ) if MIN_INDEX < MAX_INDEX else sum(LST[MAX_INDEX + 1: MIN_INDEX])
    print(f'Сумма элементов между минимальным {MIN} '
          f'и максимальным {MAX} элементами: {SUMM}')
except ValueError as err:
    print(f'Ошибка ввода: {err}')
