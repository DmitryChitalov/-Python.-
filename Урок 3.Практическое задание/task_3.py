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
INPUT = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
MAX_NUMBER = 0
MAX_INDEX = 0
MIN_NUMBER = 100000
MIN_INDEX = 0
for I in range(0, len(INPUT)):
    if INPUT[I] > MAX_NUMBER:
        MAX_NUMBER = INPUT[I]
        MAX_INDEX = I
    if INPUT[I] < MIN_NUMBER:
        MIN_NUMBER = INPUT[I]
        MIN_INDEX = I
INPUT[MAX_INDEX] = MIN_NUMBER
INPUT[MIN_INDEX] = MAX_NUMBER
# INPUT[MAX_INDEX], INPUT[MIN_INDEX] = INPUT[MIN_INDEX], INPUT[MAX_INDEX]
print(INPUT)
