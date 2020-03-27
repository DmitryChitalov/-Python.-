"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

if r[min_index_1] != r[min_index_2]:
    print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')
else:
    print(f'Элементы одинаковы и равны = {r[min_index_1]}')

'''Cортировка списка

sort_list = []
sort_list.extend(r)
sort_list.sort()
if sort_list[0] != sort_list[1]:
    print(
    f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}'
    )
else:
    print(f'Элементы одинаковы и равны = {sort_list[0]}')'''