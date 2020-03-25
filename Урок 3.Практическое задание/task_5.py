"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
from random import randint
BASE_LIST = []
NUMBER_LIST = 10
for i in range(NUMBER_LIST):
    BASE_LIST.append(randint(-100, 100))
TEMP_LIST = []
for el in BASE_LIST:
    if el < 0:
        TEMP_LIST.append(el)
MAX_NEGATIVE = max(TEMP_LIST)
IDX_MAX_NEGATIVE = BASE_LIST.index(MAX_NEGATIVE)
print(f'Базовый список: {BASE_LIST}')
print(
    f'Максимальный отрицательный элемент в данном массиве - '
    f'{MAX_NEGATIVE}, его индекс - {IDX_MAX_NEGATIVE}')
