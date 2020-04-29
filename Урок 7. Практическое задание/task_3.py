"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
import timeit
import statistics


def find_median(arr):
    for i in range(len(arr)):
        small = equal = big = 0
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                small += 1
            elif arr[i] > arr[j]:
                big += 1
            else:
                equal += 1
        equal -= 1

        if small == big or small == equal + big or big == small + equal or \
                (equal > 1 and abs(big - small) < equal):
            return arr[i]


SIZE = 5
LIMIT = 100
my_arr = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(my_arr)
print(f'медиана: {find_median(my_arr)}')
print(timeit.timeit("find_median(my_arr)", number=1000, globals=globals()))  # 0.009351991999999996

"""
ниже решение с помощью инструмента модуля statistics, работает в 10 раз быстрее
"""
print(f'\n\n{my_arr}')
print(f'Медиана = {statistics.median(my_arr)}')
print(timeit.timeit('statistics.median(my_arr)', number=1000, globals=globals()))  # 0.0009106200000000009




