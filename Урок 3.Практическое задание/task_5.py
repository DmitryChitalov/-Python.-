"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

import random


START_RANGE = -100
END_RANGE = -1
SIZE_RANGE = 10

MY_LIST = [random.randint(START_RANGE, END_RANGE) for _ in range(SIZE_RANGE)]
print(MY_LIST)

i = 0
index = -1

for i in range(len(MY_LIST)):
    if MY_LIST[i] < 0 and index == -1:
        index = i
    elif 0 > MY_LIST[i] > MY_LIST[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимально отрицательное число = {MY_LIST[index]}\n'
          f'Его элемент = {index}')
