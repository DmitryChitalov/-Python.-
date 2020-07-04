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


def merge(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge(left_half)
        merge(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i = i + 1
            else:
                lst[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1
    return lst

try:
    n = int(input("Введите число элементов: "))
except ValueError:
    print('Ошибка ввода, Введите цифру')

LST = [random.random()*50 for i in range(n)]

print(f"Стартовый массив - {LST}")
NEW_LST = merge(LST)
print(f"Исходный массив - {NEW_LST}")