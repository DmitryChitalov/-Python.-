"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random


def some_min_el(cutter, args):
    cutter = cutter
    min_list = []
    while cutter > 0:
        min = args[0]
        for el in args:
            if el <= min:
                min_list.append(el)
                cutter -= 1
                args.remove(el)
    return ' '.join(str(el) for el in min_list)

# cutter = int(input('Enter the num of required minimum values: '))
cutter = 2
preset_arr = []


for el in [i for i in range(random.randint(1, 5), random.randint(25, 54))]:
    preset_arr.append(el)


print(f'Minimum values ​​of the generated array: '
      f'{some_min_el(cutter, preset_arr)}')
