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
from random import randint
LIST = []
N = int(input("Введите количество элементов массива: "))
for i in range(N):
    LIST.append(randint(-100, 100))
print(LIST)
index_of_min = 0
index_of_max = 0
for i in range(1, len(LIST)):
    if LIST[i] > LIST[index_of_max]:
        index_of_max = i
    if LIST[i] < LIST[index_of_min]:
        index_of_min = i
LIST[index_of_min], LIST[index_of_max] = LIST[index_of_max], LIST[index_of_min]
print(LIST)
