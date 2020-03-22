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
from random import randint

MY_LIST = [randint(-100, 100) for i in range(20)]
MAX = 0
MIN = 0

for i in MY_LIST:
    if i > MAX:
        MAX = i
    if i < MIN:
        MIN = i

print(f'В списке\n'
      f'{MY_LIST}\n'
      f'Максимальное число {MAX} на {MY_LIST.index(MAX)} позиции\n'
      f'Минимальное число {MIN} на {MY_LIST.index(MIN)} позиции\n')

MY_LIST[MY_LIST.index(MAX)], MY_LIST[MY_LIST.index(MIN)] = MY_LIST[MY_LIST.index(MIN)], MY_LIST[MY_LIST.index(MAX)]

print(f'Поменяем их местами, теперь\n'
      f'Максимальное число {MAX} на {MY_LIST.index(MAX)} позиции\n'
      f'Минимальное число {MIN} на {MY_LIST.index(MIN)} позиции\n'
      f'{MY_LIST}')
