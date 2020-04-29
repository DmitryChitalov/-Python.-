"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

import random

random_list = [random.randint(-10, 10) for _ in range(10)]
min_in_list = -float('inf')

for i, item in enumerate(random_list):
    if min_in_list < item < 0:
        min_in_list = item
        min_index = i

for i in range(len(random_list)):
    if i == min_index:
        print(f'\033[33m{random_list[i]}\033[0m', end=" ")
    else:
        print(random_list[i], end=" ")

print(f'\nМинимальный отрицательный элемент {min_in_list} с индексом {min_index}')