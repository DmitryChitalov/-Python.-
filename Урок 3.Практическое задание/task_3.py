"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
from random import randint

NUMBER_ELEMS = 10
TEST_LIST = []
for i in range(NUMBER_ELEMS):
    TEST_LIST.append(randint(-100, 100))
RES_LIST = TEST_LIST[:]
MAX_NUM = max(RES_LIST)
MIN_NUM = min(RES_LIST)
IDX_MAX = RES_LIST.index(MAX_NUM)
IDX_MIN = RES_LIST.index(MIN_NUM)
RES_LIST[IDX_MAX] = MIN_NUM
RES_LIST[IDX_MIN] = MAX_NUM

print(
    f'В данном массиве чисел {TEST_LIST} максимальное число {MAX_NUM} стоит на ')
print(f'{IDX_MAX} позиции, а минимальное число {MIN_NUM} стоит на {IDX_MIN} позиции')
print(f'Заменяем их')
print(
    f'В данном массиве чисел {RES_LIST} максимальное число {MAX_NUM} стоит на')
print(f'{IDX_MIN} позиции, а минимальное число {MIN_NUM} стоит на {IDX_MAX} позиции')
