"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

import random

# Генерирование элементов масива
ARRAY_NUMBERS = [random.randint(-100, 100) for _ in range(20)]
print(f'Массив случайных целых чисел: {ARRAY_NUMBERS}')
# Находим минимальный элемент массива
MIN_VALUE_1, COUNT_MIN_1 = min((MIN_VALUE_1, ARRAY_NUMBERS.count(MIN_VALUE_1))
                               for (IDX_MIN_1, MIN_VALUE_1) in enumerate(ARRAY_NUMBERS))
print(f'Наименьший элемент {MIN_VALUE_1} встречается в этом массиве {COUNT_MIN_1} раз')
# Если наименьший элемент не повторяется в массиве ищем второй ниминмальный элемент
if COUNT_MIN_1 == 1:
    MIN_VALUE_2, COUNT_MIN_2 = min((MIN_VALUE_2, ARRAY_NUMBERS.count(MIN_VALUE_2))
                                   for (IDX_MIN_2, MIN_VALUE_2) in enumerate(ARRAY_NUMBERS)
                                   if MIN_VALUE_2 != MIN_VALUE_1)
    print(f'Второй наименьший элемент {MIN_VALUE_2} встречается в этом массиве {COUNT_MIN_2} раз')
