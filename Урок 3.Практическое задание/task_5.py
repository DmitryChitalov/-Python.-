"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
from random import randint


def negative_maximum(array):
    temp_array = [i for i in array if i < 0]
    maximum = temp_array[0]
    for i in temp_array:
        if i > maximum:
            maximum = i
    return maximum


MY_LIST = [randint(-100, 100) for i in range(14)]
MAX = negative_maximum(MY_LIST)
print(f'Базовый список: {MY_LIST}\n'
      f'Максимальный отрицательный элемент в данном массиве = {MAX}, его индекс {MY_LIST.index(MAX)}')
