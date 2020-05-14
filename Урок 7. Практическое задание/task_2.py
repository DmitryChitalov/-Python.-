"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random
from timeit import timeit


m = int(input('Введите длину массива m = '))
array = [random() * 50 for _ in range(m)]
print('Несортированный массив:', array, sep='\n\t')

def sort_merge(array):
    if len(array) > 1:
        center = len(array) // 2
        right = array[center:]
        left = array[:center]

        sort_merge(right)
        sort_merge(left)

        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
            else:
                array[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1

sort_merge(array)
print('Cортированный по возрастанию массив:', array, sep='\n\t')

print(f'\nВремя сортировки массива из {m} символов функцией (sort_merge): ',
      format(timeit('sort_merge(array)', setup='from __main__ import sort_merge, array', number=1000), '.3f'), 'сек')

# По сравнению с неоптимизированным "пузырьком" скорость выполнения задачи растет не столь массивно ( 0.400 сек - 100 символов, 38.175 сек - 1000 символов).
# Применение возможно в зависимости от технических условий поставленной задачи.


# 100
# Время сортировки массива из 100 символов функцией (sort_merge):  0.164 сек

# 1000
# Время сортировки массива из 1000 символов функцией (sort_merge):  2.035 сек