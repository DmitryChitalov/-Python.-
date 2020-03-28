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

# ВАРИАНТ №1
#ARRAY = input("Введите массов через запятую: ").split(",")
ARRAY = "8,3,15,6,4,2".split(",")
RESULT = []
for I, _ in enumerate(ARRAY):
    if int(ARRAY[I]) % 2 == 0:
        RESULT.append(I)
print("Вариант №1:", RESULT)

# ВАРИАНТ №2 - В одну строку получилось!!!
print(
    "Вариант №2:", [
        I for I, _ in enumerate(ARRAY) if int(
            ARRAY[I]) %
        2 == 0])
