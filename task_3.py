"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
"""
import random as rnd
from statistics import median
from timeit import timeit

src = [rnd.randint(1, 100) for _ in range(1, 6000)]

def find_med_v1(arr):
    return median(src)

def find_med_v2(arr):
    return sorted(arr)[len(arr) // 2]

def find_med_v3(arr):
    cnt_ge, cnt_le = 0, 0
    i, j = 0, 0
    ln = len(arr)
    while i < ln:
        for j in range(0, ln):
            if i == j:
                continue
            if arr[i] >= arr[j]:
                cnt_ge +=1
            if arr[i] <= arr[j]:
                cnt_le +=1
        if cnt_ge >= ln // 2 and cnt_le >= ln // 2:
            return arr[i]
        else:
            i += 1
            cnt_ge, cnt_le = 0, 0
            continue

print(find_med_v1(src))
print(find_med_v2(src))
print(find_med_v3(src))

print(timeit("find_med_v1(src)", setup="from __main__ import find_med_v1, src", number=1))
print(timeit("find_med_v2(src)", setup="from __main__ import find_med_v2, src", number=1))
print(timeit("find_med_v3(src)", setup="from __main__ import find_med_v3, src", number=1))

"""
Fastest way using "median" from "statistics"    0.0006178999999999768
Litlle bit worse using "sorted"                 0.0006308000000000147
My realization is nightmare :)                  0.058788599999999996
"""
