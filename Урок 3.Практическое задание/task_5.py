"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
'''
Вспомнил, что просили по минимум использовать готовые методы,
написал фукцию поиска минимального числа.
'''
def min_el(*args):
    min = 0
    for el in args:
        if el < min:
            min = el
    return min


test_arr = [
    -1, -2, -45,
    -78, -4, -1024,
    -78, -69, -7
]


print(f' The minimum element of the array is {min(test_arr)} '
      f'located at the {test_arr.index(min(test_arr)) + 1} position.')

print(f' The minimum element of the array is {min_el(*test_arr)} '
      f'located at the {test_arr.index(min_el(*test_arr)) + 1} position.')
