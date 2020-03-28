"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
INPUT = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
MIN_NUMBER_1 = 1000
MIN_NUMBER_2 = 1000
MIN_INDEX_1 = 0

for I in range(0, len(INPUT)):
    if INPUT[I] <= MIN_NUMBER_1:
        MIN_NUMBER_1 = INPUT[I]
        MIN_INDEX_1 = I
for I in range(0, len(INPUT)):
    if I != MIN_INDEX_1:
        if INPUT[I] <= MIN_NUMBER_2:
            MIN_NUMBER_2 = INPUT[I]

print("Исходный массив: ", INPUT)
COUNT = 2 if MIN_NUMBER_1 == MIN_NUMBER_2 else 1
print("Наименьший элемент: ", MIN_NUMBER_1, "встречается в этом массиве", COUNT, "раз")
if COUNT == 1: print("Второй наименьший элемент:", MIN_NUMBER_2)
