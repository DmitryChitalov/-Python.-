"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


try:
    NUM_1 = float(input("Введите число: "))
    NUM_2 = float(input("Введите число: "))
    NUM_3 = float(input("Введите число: "))
    if NUM_1 == NUM_2 or NUM_3 == NUM_1 or NUM_2 == NUM_3:
        print("Введены одинаковые числа")
    else:
        if NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
            print("Среднее значение ", NUM_2)
        elif NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
            print("Среднее значение ", NUM_1)
        else:
            print("Среднее значение ", NUM_3)
except ValueError:
    print("Неверно введено число")
