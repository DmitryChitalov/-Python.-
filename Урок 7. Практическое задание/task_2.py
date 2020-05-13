"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random

random_range = 50


def task7_2(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    left_el = task7_2(arr[:len(arr) // 2])
    right_el = task7_2(arr[len(arr) // 2:])
    i, j = 0, 0
    while len(left_el) > i and len(right_el) > j:
        if left_el[i] < right_el[j]:
            arr[i + j] = left_el[i]
            i += 1
        else:
            arr[i + j] = right_el[j]
            j += 1
    while len(left_el) > i:
        arr[i + j] = left_el[i]
        i += 1
    while len(right_el) > j:
        arr[i + j] = right_el[j]
        j += 1
    return arr

while(1):
    try:
        user_input = int(input('Введите число элементов: '))
        rand_data = [round(random.uniform(0, random_range), 2) for _ in range(user_input)]
        print('Исходный массив:', rand_data)
        task7_2(rand_data)
        print('Отсортированный:', rand_data)
        break
    except:
        print('Ошибка ввода')


