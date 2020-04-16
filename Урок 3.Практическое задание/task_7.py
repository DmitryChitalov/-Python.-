"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""


from random import randint

mylist = [randint(-100, 100) for i in range(0, 10)]

min1 = min(mylist)
min1_idx = mylist.index(min1)
min1_count = mylist.count(min1)
min2 = min(mylist[:min1_idx] + mylist[min1_idx + 1:])
min2_idx = mylist.index(min2)
min2_count = mylist.count(min2)

print(f"Исходный массив: {mylist}")
print(f"Наименьший элемент: {min1}, встречается в этом массиве {min1_count} раз")
print(f"Второй наименьший элемент: {min2}, встречается в этом массиве {min2_count} раз")

