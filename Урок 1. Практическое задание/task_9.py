"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

NUMB_A = int(input('Введите первое число: '))
NUMB_B = int(input('Введите второе число: '))
NUMB_C = int(input('Введите третье число: '))

if NUMB_B < NUMB_A < NUMB_C:
    print(NUMB_A)
else:
    if NUMB_A < NUMB_B < NUMB_C:
        print(NUMB_B)
    else: print(NUMB_C)



