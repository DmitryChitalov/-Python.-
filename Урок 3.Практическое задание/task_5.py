"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
from random import random
from random import randint

N = 15
INPUT = [0] * N
for i in range(N): INPUT[i] = randint(-10, 10)
print(INPUT)

MAX_NUMBER = -1000
MAX_INDEX = 0
for i, item in enumerate(INPUT):
    if item < 0:
        if MAX_NUMBER < item:
            MAX_NUMBER = item
            MAX_INDEX = i
print(MAX_NUMBER, MAX_INDEX)
