"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import randint

a = [randint(-10, 10) for x in range(1, 10)]
print(a)
cnt = 0
min_one = 99
min_two = 100
for i in a:
    if i < min_one:
        min_one = i
a.remove(min_one)
for i in a:
    if i == min_one:
        cnt = 2
    elif i < min_two:
        min_two = i
if cnt == 2:
    print(f'Минимальное число {min_one}, встречается в массиве 2 раза')
else:
    print(f'Минимальное число {min_one}, второе минимальное число {min_two}')
