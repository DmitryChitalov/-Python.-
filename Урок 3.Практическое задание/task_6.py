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

MY_LIST = [randint(0, 100) for i in range(10)]
print(f'Исходный список {MY_LIST}')

INDX_1 = max(MY_LIST)
INDX_2 = min(MY_LIST)
SUMM = 0
# print(f'{MY_LIST.index(INDX_1)}, {MY_LIST.index(INDX_2)}')
if MY_LIST.index(INDX_1) > MY_LIST.index(INDX_2):
    for i in range(MY_LIST.index(INDX_2) + 1, MY_LIST.index(INDX_1)):
        SUMM += MY_LIST[i]
else:
    for i in range(MY_LIST.index(INDX_1) + 1, MY_LIST.index(INDX_2)):
        SUMM += MY_LIST[i]
print(
    f'Сумма элементов между минимальным {INDX_2} и максимальным {INDX_1} элементами: {SUMM}')
