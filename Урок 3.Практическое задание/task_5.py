"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
from random import random


def my_list():
    """делает список"""

    n = int(input('введите количество элементов в списке: '))
    if n == 0:
        my_list = []
        return my_list
    while True:
        my_list = []
        k = 0
        for _ in range(n):
            number = int(random() * 100)
            j = int(random() * 100)
            if j <= 20:
                number *= -1
                my_list.append(number)
                k = 1
            else:
                my_list.append(number)
        if k:
            break
    return my_list


my_list = my_list()
if my_list:
    my_list_1 = [x for x in my_list if x < 0]
    # находим число и индкхс
    number = min(my_list_1, key=abs)
    index = my_list_1.index(number)

    print(f'Базовый список: {my_list}\n')
    print(f'Максимальный отрицательный элемент в данном массиве = {number} его индекс: {index}\n')
else:
    print(f'список пуст')
