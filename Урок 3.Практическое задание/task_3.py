"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
import random

# вариант 1
min_int = -100
max_int = 100
user_arr = [random.randint(min_int, max_int) for i in range(10)]
print(user_arr)

max_int = max(user_arr)
min_int = min(user_arr)
idx_max = user_arr.index(max_int)
idx_min = user_arr.index(min_int)
print(max_int)
print(min_int)
print(idx_max)
print(idx_min)
user_arr[idx_max], user_arr[idx_min] = min_int, max_int
print(min_int, max_int)
idx_max = user_arr.index(max_int)
idx_min = user_arr.index(min_int)
print(user_arr)

# вариант 2
user_arr_2 = [random.randint(min_int, max_int) for i in range(10)]
print(user_arr_2)
idx_min_2 = 0
idx_max_2 = 0
for i in range(len(user_arr_2)):
    if user_arr_2[i] < user_arr_2[idx_min_2]:
        idx_min_2 = i
    elif user_arr_2[i] > user_arr_2[idx_max_2]:
        idx_max_2 = i

user_arr_2[idx_min_2], user_arr_2[idx_max_2] = user_arr_2[idx_max_2], user_arr_2[idx_min_2]
print(user_arr_2)
