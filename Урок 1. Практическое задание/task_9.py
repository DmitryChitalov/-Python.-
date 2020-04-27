"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

NUMBER_1 = float(input("Введите первое число: "))
NUMBER_2 = float(input("Введите второе число: "))
NUMBER_3 = float(input("Введите третье число: "))
if NUMBER_1 == NUMBER_2 == NUMBER_3:
    print("Все числа равны")
elif NUMBER_1 < NUMBER_2 < NUMBER_3:
    print("Среднее число: ", str(NUMBER_2))
elif NUMBER_2 < NUMBER_3 < NUMBER_1:
    print("Среднее число: ", str(NUMBER_3))
else:
    print("Среднее число: ", str(NUMBER_1))
