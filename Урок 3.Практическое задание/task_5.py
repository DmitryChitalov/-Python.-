"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

import random

LIST_N = [random.randint(-100, 100) for i in range(10)]

print(f"Базовый список: {LIST_N}")

NUMBER_MAX = None
INDEX_MAX = None

for i in range(len(LIST_N)):

    if LIST_N[i] < 0:
        if (INDEX_MAX is None) or LIST_N[i] > NUMBER_MAX:
            NUMBER_MAX = LIST_N[i]
            INDEX_MAX = i

if INDEX_MAX is None:
    print(f"В данном массиве нет отрицательных значений")
else:
    print(f"Максимальный отрицательный элемент в массиве = {NUMBER_MAX}, его индекс {INDEX_MAX}")
