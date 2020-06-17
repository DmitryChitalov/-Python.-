"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

from random import randint

MASSIVE = [randint(-100, 100) for el in range(randint(0, 20))]
NEGATIVE_ELS = [el for el in MASSIVE if el < 0]
MAX_NEGATIVE_EL = max([el for el in MASSIVE if el < 0]) if len(NEGATIVE_ELS) > 0 else 'отсутсвует'
MAX_NEGATIVE_IDX = MASSIVE.index(MAX_NEGATIVE_EL) if len(NEGATIVE_ELS) > 0 else 'отсутствует'

print(f"Базовый список: {MASSIVE} Максимальный отрицательный элемент в данном массиве = "
      f"{MAX_NEGATIVE_EL}, его индекс = {MAX_NEGATIVE_IDX}")
