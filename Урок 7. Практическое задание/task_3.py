"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random

M = int(input("Введите число М для масива 2m + 1: "))
MAS = [random.randint(-100, 100) for _ in range(2 * M + 1)]

print('Массив', MAS)
print('Сортированный массив', sorted(MAS))
print("Медиана массива: ", sorted(MAS)[M])

# Как сделать без сортировки недодумался
