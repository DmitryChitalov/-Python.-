"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import randint

g = int(input('введите колличество элементов в массиве: '))
list = [randint(-50, 50) for i in range(g)]
print(f'Массив: \n{list}')
minimal = 0

for i in range(2):
    if i > 0:
        if minimal != min(list):
            minimal = min(list)
            print(f'Второй наименьший элемент: {minimal}')
            list.remove(minimal)
        else:
            print(f'Встречается в этом массиве 2 раз')
    else:
        minimal = min(list)
        print(f'Наименьший элемент: {minimal}')
        list.remove(minimal)