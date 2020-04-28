"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

Подсказка:
Попробуйте решить эту задачу в одну строку (такое решение точно есть)

Пример:
Исходный массив: [8, 3, 15, 6, 4, 2], результат: [0, 3, 4, 5]
"""

import random

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)

def odd_indexes(array, result=[]):
    """ Finds indexes of even items in array """
    for index, element in enumerate(array):
        if element % 2 == 0:
            result.append(index)
    return result

print(odd_indexes(EXAMPLE))
