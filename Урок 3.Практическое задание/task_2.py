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

# создаем список из условия
SOURCE_LIST = [8, 3, 15, 6, 4, 2]

# создаем список для записи значений, удовлетворяющих условию,
# что элемент первого списка является четный, поэтому записываем
# его индекс в цикле
RESULT_LIST = [idx for idx in range(len(SOURCE_LIST)) if SOURCE_LIST[idx] % 2 == 0]

# выводим результирующий список на экран
print(RESULT_LIST)
