"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

LST = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
# Чтобы воспользоваться автозаполнением массива, раскомментируйте 4 строки ниже
# from random import randint
# LENGTH = 10 # количество элементов списка
# FROM, TO = -100, 100 # диапазон значений для randint()
# LST = [randint(FROM, TO) for i in range(LENGTH)]
print(LST)
NUM = max(filter(lambda x: x < 0, LST))
IDX = LST.index(NUM)
print(f'Максимальный отрицательный элемент '
      f'в данном массиве: {NUM}, его индекс: {IDX}')
