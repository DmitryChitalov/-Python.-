"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

import random

random_list = [random.randint(0, 101) for _ in range(10)]

min_first, min_second = (0, 1) if random_list[0] > random_list[1] else (1, 0)

for i in range(2, len(random_list)):
    if random_list[i] < random_list[min_first]:
        temp = min_first
        min_first = i
        if random_list[temp] < random_list[min_second]:
            min_second = temp

    elif random_list[i] < random_list[min_second]:
        min_second = i
print('Исходный массив :')
for i in range(len(random_list)):
    if i == min_first:
        print(f'\033[33m{random_list[i]}\033[0m', end=" ")
    elif i == min_second:
        print(f'\033[31m{random_list[i]}\033[0m', end=" ")
    else:
        print(random_list[i], end=" ")
print('\n')
print(f'Наименьший элемент {random_list[min_first]} с индексом {min_first}')
print(f'Второй наименьший элемент {random_list[min_second]} с индексом {min_second}')