"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""


from random import random
N = 10
arrplus = [0] * N
arrminus = [0] * N
arrsourse = []
even = []
amin = 0
amax = 0
for i in range(N):
    arrplus[i] = int(random() * 35)
for k in range(N):
    arrminus[k] = int(random() * - 35)
arr = arrminus + arrplus

for h in range(len(arr)):
    if arr[h] < 0:
        arrsourse.append(arr[h])
amax = max(arrsourse)
amaxindex = arr.index(amax)
print('Исходный массив: ', arr)
print(f'максимальное число из отрицательный {amax} находиться на позиции {amaxindex}')

