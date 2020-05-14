"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

#Comment: Хотелось придумать что-то свое, но не получилось:)

import random

n = int(input('Введите количество элементов: '))
my_array = [random.random() * 50 for i in range(n)]
print(my_array)


def merge(array):
    if len(array) > 1:
        k = len(array) // 2
        arr1 = array[:k]
        arr2 = array[k:]
        merge(arr1)
        merge(arr2)
        i = 0
        j = 0
        l = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array[l] = arr1[i]
                i += 1
            else:
                array[l] = arr2[j]
                j += 1
            l += 1

        while i < len(arr1):
            array[l] = arr1[i]
            i += 1
            l += 1

        while j < len(arr2):
            array[l] = arr2[j]
            j += 1
            l += 1
        return array

print(merge(my_array))
