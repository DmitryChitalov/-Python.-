"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random, statistics
m = int(input("Введите натуральное число: "))
data_list = [random.randint(0, 1000) for _ in range(2 * m + 1)]

def my_median(explored_list):
    lower_list, higher_list = [], []
    try_med = 0
    for i in range(len(explored_list)):
        try_med += explored_list[i]
    try_med /= len(explored_list)
    #print(f"try_med = {try_med}")
    for i in range(len(explored_list)):
        if explored_list[i] <= try_med:
            lower_list.append(explored_list[i])
        if explored_list[i] >= try_med:
            higher_list.append(explored_list[i])
    while len(lower_list) > len(higher_list):
        higher_list.append(max(lower_list))
        lower_list.remove(max(lower_list))
    while len(lower_list) < len(higher_list):
        lower_list.append(min(higher_list))
        higher_list.remove(min(higher_list))
    #print(sorted(lower_list))
    #print(sorted(higher_list))
    if  len(lower_list) > len(higher_list):
        try_med = max(lower_list)
    else:
        try_med = min(higher_list)
    return try_med


print(data_list)
print(f"Моя медиана {my_median(data_list)}")
print(f"Встроенная медиана {statistics.median(data_list)}")
