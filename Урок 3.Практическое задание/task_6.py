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

while True:
    try:
        COUNT = int(input('Введите количество элементов в массиве:'))
        break
    except ValueError:
        print('Вы ввели не число')

NUM_LIST = [randint(0, 100) for i in range(COUNT)]
MIN_NUM = NUM_LIST[0]
MAX_NUM = NUM_LIST[0]
MIN_INDEX = 0
MAX_INDEX = 0
for i, el in enumerate(NUM_LIST):
    if el > MAX_NUM:
        MAX_NUM = el
        MAX_INDEX = i
    if el < MIN_NUM:
        MIN_NUM = el
        MIN_INDEX = i

if MAX_INDEX > MIN_INDEX:
    SUM_NUM = sum(NUM_LIST[MIN_INDEX + 1:MAX_INDEX])
else:
    SUM_NUM = sum(NUM_LIST[MAX_INDEX + 1:MIN_INDEX])

print(f'Массив: {NUM_LIST}')
print(f'Сумма между минимальным ({MIN_NUM}) и максимальным ({MAX_NUM}) элементами: {SUM_NUM}')
