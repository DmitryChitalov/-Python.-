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
# Решение в одну строку, как вы и просили, все остальное "обвязка"
import random

while True:
    N = input(
        'Сгенерировать случайный массив и сохранить индексы его четных элементов Y/N: ')
    if N == "Y":
        ARR = [random.randint(0, 20) for i in range(20)]
        A = [ARR.index(i) for i in ARR if i % 2 == 0]  # решение
        print(f"В массиве {ARR}")
        print(f"Четные элементы находятся по следующим индексам: {A}")
    if N == "N":
        N = input('Вы уверены? Для выхода из программы нажмите: Q ')
        if N == "Q":
            break
