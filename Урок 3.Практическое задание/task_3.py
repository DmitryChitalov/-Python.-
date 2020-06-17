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
initial_list = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]

in_max = 0
in_min = 0

for x in range(len(initial_list)):
    if initial_list[x] < initial_list[in_min]:
        in_min = x
    elif initial_list[x] > initial_list[in_max]:
        in_max = x
print(f"Minimal number is: {initial_list[in_min]} index was {in_min}")
print(f"Maximum number is: {initial_list[in_max]} index was {in_max}")
initial_list[in_max], initial_list[in_min] = initial_list[in_min], initial_list[in_max]
print(initial_list)
