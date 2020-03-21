"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

Подсказка:
Попробуйте решить эту задачу в одну строку (такое решение точно есть)

Пример:
Исходный массив: [8, 3, 15, 6, 4, 2], результат: [0, 3, 4, 5]
"""

from random import randint

# Генерируем список уникальных случайных чисел. С не уникальными
# мой генератор списков будет не корректно работать, иначе не вышло
# придумать решение в одну строку

LIST = list(set([randint(1, 100) for i in range(20)]))
NEW_LIST = [LIST.index(itm) for itm in LIST if itm % 2 == 0]
print(f'Исходный массив: {LIST}')
print(f'Результат: {NEW_LIST}')

# Реализация в несколько строк но учитывающая повторяющиеся элементы в списке

# VALUE = int(input('Введите количество чисел в массиве: '))
# LIST = [randint(1, 100) for i in range(VALUE)]
# NEW_LIST = []
#
# for itm in list(range(0, VALUE - 1)):
#     if LIST[itm] % 2 == 0:
#         NEW_LIST.append(itm)
# print(f'Исходный массив: {LIST}')
# print(f'Результат: {NEW_LIST}')
