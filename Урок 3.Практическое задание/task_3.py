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
from random import random

N = int(input("Введите длину массива: "))
my_arr = []
for i in range(N):
    my_arr.append(int(random()*100)-50)
print(my_arr)
min_arr = min(my_arr)
max_arr = max(my_arr)
min_index = my_arr.index(min_arr)
max_index = my_arr.index(max_arr)
print(f"Максимальное значение массива {max_arr} c индексом {max_index}, минимальное значение - {min_arr} с индексом {min_index}")
my_arr[min_index], my_arr[max_index] = my_arr[max_index], my_arr[min_index]
print(my_arr)