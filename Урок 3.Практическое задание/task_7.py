"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""


from random import randint


def min_value(array, min_el=None):
    min_val = array[0]
    if min_el is None:
        for el in array:
            if min_val > el:
                min_val = el
    else:
        for el in array:
            if min_val > el > min_el:
                min_val = el
    return min_val


# EXAMPLE = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73, -86]
EXAMPLE = [randint(-100, 100) for i in range(0, 10)]
MIN_EL = min_value(EXAMPLE)

print(f"Базовый список: {EXAMPLE}")
if EXAMPLE.count(MIN_EL) > 1:
    print(f"Наименьший элемент и второй наименьший элемент равны: {MIN_EL} ")
else:
    SEC_MIN_EL = min_value(EXAMPLE, MIN_EL)
    print(f"Наименший элемент: {MIN_EL}\nВторой наименьший элемент: {SEC_MIN_EL}")
