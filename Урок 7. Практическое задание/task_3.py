"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random, numpy

m = int(input('Введите m: '))
list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(list)
print(numpy.median(list))

def selection_median(list, m):
    for i in range(m):
        list.remove(min(list))

    return min(list)


print(selection_median(list, m))

list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(list)
print(numpy.median(list))

def sorted_median(list, m):
    list = sorted(list)
    return list[m]

print(sorted_median(list, m))