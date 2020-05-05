"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint
import timeit


def without_sort(arr):
    n = 0
    while n < len(arr):
        more = []
        less = []
        for element in range(len(arr)):
            if arr[n] > arr[element]:
                less.append(arr[element])
            elif arr[n] < arr[element]:
                more.append(arr[element])
        n += 1
        if len(more) == len(less):
            break
    return f'Медиана данного массива - {arr[n - 1]}'


NUM = int(input("Размер массива рассчитывается по формуле 2m + 1: \nВведите m: "))
ARR = [randint(-100, 100) for _ in range(NUM * 2 + 1)]
print(f'Исходный массив - {ARR}')
print(without_sort(ARR))

print(timeit.timeit("without_sort(ARR)", \
    setup="from __main__ import without_sort, ARR", number=10))
print(timeit.timeit("without_sort(ARR)", \
    setup="from __main__ import without_sort, ARR", number=100))
print(timeit.timeit("without_sort(ARR)", \
    setup="from __main__ import without_sort, ARR", number=1000))
