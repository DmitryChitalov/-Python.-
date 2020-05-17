"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform

source = [uniform(0, 50) for i in range(5)]
print('Исходный - ', source)


def merge(left, right):
    result = []
    i = 0
    y = 0
    while i < len(left) and y < len(right):
        if left[i] <= right[y]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[y])
            y += 1
    result += left[i:] + right[y:]
    return result


def sort(source):
    if len(source) <= 1:
        return source
    else:
        left = source[:len(source) // 2]
        right = source[len(source) // 2:]
    return merge(sort(left), sort(right))


print('Отсортированный -', sort(source))
