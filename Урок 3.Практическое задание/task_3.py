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

random_list = [random.randint(0, 100) for _ in range(10)]
random.shuffle(random_list)

print('\nИсходный массив :')
print(*random_list)
min_in_list = random_list[0]
max_in_list = random_list[1]

for i, item in enumerate(random_list):
    if item <= min_in_list:
        min_in_list = item
        min_index = i
    if item >= max_in_list:
        max_in_list = item
        max_index = i

random_list[min_index] = max_in_list
random_list[max_index] = min_in_list

print('\nОтсортированный массив :')
for i in range(len(random_list)):
    if i == min_index:
        print(f'\033[33m{random_list[i]}\033[0m', end=" ")
    elif i == max_index:
        print(f'\033[31m{random_list[i]}\033[0m', end=" ")
    else:
        print(random_list[i], end=" ")

print (f'\n\nМинимальный элемент в массиве : [{min_index}] - {min_in_list}')
print (f'Максимальный элемент в массиве: [{max_index}] - {max_in_list}')