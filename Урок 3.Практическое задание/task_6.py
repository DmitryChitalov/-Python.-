"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

import random

min_index = 0
max_index = 0

random_list = [random.randint(0, 101) for _ in range(10)]

for el in range(1, len(random_list)):
    if random_list[el] < random_list[min_index]:
        min_index = el
    elif random_list[el] > random_list[max_index]:
        max_index = el

if min_index > max_index:
    min_index, max_index = max_index, min_index

for i in range(len(random_list)):
    if i == min_index:
        print(f'\033[33m{random_list[i]}\033[0m', end=" ")
    elif i == max_index:
        print(f'\033[31m{random_list[i]}\033[0m', end=" ")
    else:
        print(random_list[i], end=" ")

print(f'\n\nЛевая граница: {random_list[min_index]}\n'
      f'Правая граница: {random_list[max_index]}')

summ = 0
for el in range(min_index + 1, max_index):
    summ += random_list[el]
if ((abs(max_index-min_index)) == 1):
    print(f'\nЭлементы соседние. Сумма = {summ}')
else:
    print(f'\nСумма между элементами с индексами {min_index} и {max_index} = {summ}')