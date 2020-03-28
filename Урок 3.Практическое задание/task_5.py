"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

A = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
B = [x for x in A if x < 0]
MAX_NEGATIVE = max(B)
print(f'Максимальный отрицательный элемент в данном массиве = {MAX_NEGATIVE},'
      f' его индекс {A.index(MAX_NEGATIVE)}')
