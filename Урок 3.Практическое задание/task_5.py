"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю
Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

import random

# Генерирование элементов массива случайными значениями целых чисел в диапазоне от -100 до 100
ARRAY_NUMBERS = [random.randint(-100, 100) for _ in range(20)]
print(f'Исходный массив элементов: {ARRAY_NUMBERS}')
# Способ № 1
MAX_NEGATIVE_NUMBER = max([el for el in ARRAY_NUMBERS if el < 0])
print(f'\r\nМаксимальный отрицательный элемент в массиве: {MAX_NEGATIVE_NUMBER}')
print(f'Позиция элемента в массиве: {ARRAY_NUMBERS.index(MAX_NEGATIVE_NUMBER)}')
print('*' * 50)
# Способ № 2 (решение в одну строку)
MAX_NEGATIVE_NUMBER, IDX_MAX_NEGATIVE = max((MAX_NEGATIVE_NUMBER, IDX_MAX_NEGATIVE)
                                            for (IDX_MAX_NEGATIVE, MAX_NEGATIVE_NUMBER)
                                            in enumerate(ARRAY_NUMBERS)
                                            if MAX_NEGATIVE_NUMBER < 0)
print(f'Максимальный отрицательный элемент в массиве: {MAX_NEGATIVE_NUMBER}')
print(f'Позиция элемента в массиве: {IDX_MAX_NEGATIVE}')
