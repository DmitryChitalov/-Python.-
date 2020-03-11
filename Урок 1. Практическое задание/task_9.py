"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

try:
    NUMBER_1 = int(input("Введите первое число\n"))
    NUMBER_2 = int(input("Введите второе число\n"))
    NUMBER_3 = int(input("Введите третье число\n"))

    if NUMBER_1 < NUMBER_2 < NUMBER_3 or NUMBER_3 < NUMBER_2 < NUMBER_1:
        MIDDLE = NUMBER_2
    elif NUMBER_1 < NUMBER_3 < NUMBER_2 or NUMBER_2 < NUMBER_3 < NUMBER_1:
        MIDDLE = NUMBER_3
    elif NUMBER_1 == NUMBER_2 == NUMBER_3:
        MIDDLE = NUMBER_1
        print("Числа равны\n")
    else:
        MIDDLE = NUMBER_1

    print(f"Середина = {MIDDLE}")

except ValueError:
    print("Нужно ввести челое число")
