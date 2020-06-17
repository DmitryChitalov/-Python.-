# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1
i = 0
while i < len(a):
    print(i + 2, ' - ', a[i])
    i += 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

a = [8, 3, 15, 6, 4, 2]
c = []
for el in a:
    if el % 2 == 0:
        c.append(a.index(el))
print(c)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array_random = random.randint(2, 15)
array = []

for i in range(array_random):
    array.append(i)
print('random array - ', array)

array[-1], array[0] = array[0], array[-1]
print(array)

# 4. Определить, какое число в массиве встречается чаще всего.

x = 15
array = [1, 1, 1, 2, 2, 3, 4, 2, 8, 8, 8, 8, 8, 8, 1, 9]

num = array[0]
max_frq = 1
for i in range(x - 1):
    frq = 1
    for k in range(i + 1, x):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

print(f'number {num} will found {max_frq} times')

# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
arr_sort = sorted(arr)

del arr_sort[0]
del arr_sort[-1]
print(f'Massiv without first and last element - {arr_sort}')  # , arr_sort

summ = 0
for i in arr_sort:
    summ = summ + i
print(f'sum = {summ}')
