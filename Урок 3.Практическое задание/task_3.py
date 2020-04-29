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

# Вариант 1
from random import randint

M = [randint(-100, 100) for i in range(10)]
print(M)

i = M.index(max(M))
j = M.index(min(M))
M[i], M[j] = M[j], M[i]
print(M)

# проверка, когда два и более макса и мина, заменяет первые встречающиеся
M = [0, 4, 34, 23, 45, 99, 0, 99]
M[M.index(max(M))], M[M.index(min(M))] = M[M.index(min(M))], M[M.index(max(M))]
print(M)

# Вариант 2

M = [randint(-100, 100) for i in range(10)]
print(M)

MAX_IND = 0
MIN_IND = 0
for i in range(len(M)):
    if M[i] > M[MAX_IND]:
        MAX_IND = i
    elif M[i] < M[MIN_IND]:
        MIN_IND = i
M[MAX_IND], M[MIN_IND] = M[MIN_IND], M[MAX_IND]
print(M)
