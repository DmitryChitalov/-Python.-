"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random
from random import randrange


def task7_3(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    left_el = [el for el in arr if el < pivot]
    right_el = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(left_el):
        return task7_3(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return task7_3(right_el, k - len(left_el) - len(pivots))


M = randrange(10)
rand_data = [random.randint(0, 20) for _ in range(2 * M + 1)]
print(f'm - натуральное число, заполнен случайным образом: {M}')
print(f'Исходный массив: {rand_data}')
print(f'Медиана в массиве: {task7_3(rand_data, len(rand_data) / 2)}')
rand_data.sort()

print(f'\n========================Проверка==========================\n')
for i in range(len(rand_data)):
    if i == int(len(rand_data) / 2):
        print(f'\033[33m{rand_data[i]}\033[0m', end=" ")
    else:
        print(rand_data[i], end=" ")
