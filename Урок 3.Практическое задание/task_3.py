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
N = 10
arr = [0]*N
even = []
amin = 0
amax = 0
for i in range(N):
    arr[i] = int(random() * 35)
print('Исходный массив: ', arr)

amin = min(arr)
amax = max(arr)
aminindex = arr.index(amin)
amaxindex = arr.index(amax)
arr.insert(amaxindex, amin)
arr.pop(amaxindex + 1)
arr.insert(aminindex, amax)
arr.pop(aminindex + 1)
print('Получился:       ', arr)
