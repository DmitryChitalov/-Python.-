"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
from sys import exit

try:
    NUM_1 = int(input("Введите первое число: "))
    NUM_2 = int(input("Введите второе число: "))
    NUM_3 = int(input("Введите третье число: "))

    if NUM_1 == NUM_2 == NUM_3:
        print("Числа равны")
        exit(1)

    if NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
        print(f"Среднее: {NUM_1}")
    elif NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
        print(f"Среднее: {NUM_2}")
    else:
        print(f"Среднее: {NUM_3}")

except ValueError:
    print("Введены некорректные данные")

