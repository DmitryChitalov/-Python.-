"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

try:
    NUM_A = float(input('Введите первое число: '))
    NUM_B = float(input('Введите второе число: '))
    NUM_C = float(input('Введите третье число: '))

    if NUM_A == NUM_B or NUM_A == NUM_C or NUM_B == NUM_C \
            or NUM_A == NUM_B == NUM_C:
        print('Для определения среднего числа - числа должны быть разные!')
    elif NUM_B < NUM_A < NUM_C:
        print(f'Среднее число: {NUM_A}')
    elif NUM_A < NUM_B < NUM_C:
        print(f'Среднее число: {NUM_B}')
    else:
        print(f'Среднее число: {NUM_C}')
except ValueError:
    print('Необходимо вводить числа!')
