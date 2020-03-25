"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

from random import randint


EXAMPLE = [randint(-100, 100) for i in range(0, 15)]
# EXAMPLE = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
INDEX = 0
for i in range(len(EXAMPLE)):
    if EXAMPLE[i] < 0:
        if EXAMPLE[INDEX] < 0 and abs(EXAMPLE[i]) < abs(EXAMPLE[INDEX]):
            INDEX = i
        elif EXAMPLE[INDEX] > 0:
            INDEX = i

print(f"Базовый список: {EXAMPLE}\nМаксимально отрицательный элемент {EXAMPLE[INDEX]}\n"
      f"Его индекс {INDEX}")
