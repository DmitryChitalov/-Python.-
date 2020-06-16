"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

list_ = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
min_item = min(list_)

for i in list_:
    if i < 0:
        if i > min_item:
            min_item = i
print(f'Максимальный отрицательный элемент в данном массиве = {min_item}, его индекс {(list_.index(-5))}')
