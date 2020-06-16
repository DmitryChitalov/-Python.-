"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""

from random import randint


def create_array(arr_length):
    array = [randint(-99, 99) for i in range(arr_length)]
    return array


def get_max_negative(array):
    min_el = float("-inf")
    index_ = 0
    for n, el in enumerate(array):
        if min_el < el < 0:
            min_el = el
            index_ = n
    return min_el, index_


if __name__ == '__main__':
    arr = create_array(10)
    num, index = get_max_negative(arr)
    print(f"Массив: {arr}",
          f"Максимальный отрицательный элемент в массиве = {num}, его индекс {index}",
          sep="\n"
          )

# output:
# Массив: [40, 77, -72, -72, 85, 46, 61, -23, 90, -91]
# Максимальный отрицательный элемент в массиве = -23, его индекс 7

