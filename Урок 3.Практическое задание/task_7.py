"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import random


def my_list():
    """делает список"""

    n = int(input('введите количество элементов в списке: '))
    if n == 0:
        my_list = []
        return my_list
    while True:
        my_list = []
        k = 0
        for _ in range(n):
            number = int(random() * 100)
            j = int(random() * 100)
            if j <= 20:
                number *= -1
                my_list.append(number)
                k = 1
            else:
                my_list.append(number)
        if k:
            break
    return my_list


MY_LIST = my_list()
print(MY_LIST)

# жульнический вариант
MY_LIST_2 = list(sorted(MY_LIST)[:2])
if MY_LIST_2[0] == MY_LIST_2[1]:
    print(f'Наименьший элемент: {MY_LIST_2[0]}, встречается в этом массиве , больше чем 1 раз')
else:
    print(f'Наименьший элемент: {MY_LIST_2[0]}, встречается в этом массиве , 1 раз')
    print(f'Второй наименьший элемент: {MY_LIST_2[1]}')

# вариант честный
MIN_1 = MY_LIST[0]
MIN_2 = MY_LIST[0]

for i in MY_LIST_2:
    if i < MIN_1:
        MIN_1 = i
    elif i < MIN_2:
        MIN_2 = i

if MY_LIST_2[0] == MY_LIST_2[1]:
    print(f'Наименьший элемент: {MY_LIST_2[0]}, встречается в этом массиве , больше чем 1 раз')
else:
    print(f'Наименьший элемент: {MY_LIST_2[0]}, встречается в этом массиве , 1 раз')
    print(f'Второй наименьший элемент: {MY_LIST_2[1]}')
