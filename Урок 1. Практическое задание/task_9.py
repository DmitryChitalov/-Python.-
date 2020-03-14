"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

NUMBER_1 = int(input("Введите первое число: "))
NUMBER_2 = int(input("Введите второе число: "))
NUMBER_3 = int(input("Введите третье число: "))
AVERAGE_NUMBER = NUMBER_1


if NUMBER_1 < NUMBER_2 < NUMBER_3 or NUMBER_3 < NUMBER_2 < NUMBER_1:
    AVERAGE_NUMBER = NUMBER_2
elif NUMBER_1 < NUMBER_3 < NUMBER_2 or NUMBER_2 < NUMBER_3 < NUMBER_1:
    AVERAGE_NUMBER = NUMBER_3

if NUMBER_1 == NUMBER_2 or NUMBER_1 == NUMBER_3 or NUMBER_2 == NUMBER_3:
    print("Введены 2 или 3 равных чисел")
else:
    print(f"Среднее число из предоставленных: {AVERAGE_NUMBER}")
