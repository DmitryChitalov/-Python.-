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
from random import random


# делаем список
def my_list():
    """делает список"""

    n = int(input('введите количество элементов в списке: '))
    my_list = []
    for x in range(n):
        number = int(random() * 100)
        j = int(random() * 100)
        if j <= 20:
            number *= -1
            my_list.append(number)
        else:
            my_list.append(number)
    return my_list

# делаем список
MY_LIST_1 = my_list()
MY_LIST_2 = list(MY_LIST_1)  # нужен что бы выводить два разных списка

# находим минимум и макисимум
MIN_NUMBER, MAX_NUMBER = min(MY_LIST_1), max(MY_LIST_1)
MIN_INDEX, MAX_INDEX = MY_LIST_1.index(MIN_NUMBER), MY_LIST_1.index(MAX_NUMBER)

# меняем местами
MY_LIST_2[MIN_INDEX] = MAX_NUMBER
MY_LIST_2[MAX_INDEX] = MIN_NUMBER

# выводим результат


print(f'Список {MY_LIST_1}: его  минимум: {MIN_NUMBER}, на позиции: {MIN_INDEX} и максимум: '
      f'{MAX_NUMBER}, на позиции: {MAX_INDEX} \n')
print(f'Превращается в {MY_LIST_2}')
