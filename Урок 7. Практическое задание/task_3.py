"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random


def median(array):
    for i in range(len(array)):
        my_min = equal = my_max = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                my_min += 1
            elif array[i] > array[j]:
                my_max += 1
            else:
                equal += 1
        equal -= 1

        if my_min == my_max or my_min == equal + my_max or my_max == equal + my_min or \
                (equal > 1 and abs(my_max - my_min) < equal):
            return array[i]


SIZE = 4
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]

print(data)
print(f'Медиана = {median(data)}')
print(data)
print(sorted(data))

