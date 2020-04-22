"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).
"""

while True:
    try:
        NUMBER_1 = float(input('Введите первое число : '))
        NUMBER_2 = float(input('Введите второе число : '))
        NUMBER_3 = float(input('Введите третье число : '))
        if NUMBER_2 < NUMBER_1 < NUMBER_3 or NUMBER_3 < NUMBER_1 < NUMBER_2:
            print(f'Среднее число = {NUMBER_1}')
        elif NUMBER_1 < NUMBER_2 < NUMBER_3 or NUMBER_3 < NUMBER_2 < NUMBER_1:
            print(f'Среднее число = {NUMBER_2}')
        elif NUMBER_1 == NUMBER_2 and NUMBER_2 == NUMBER_3:
            print('Вы ввели одинаковые числа')
        elif NUMBER_1 == NUMBER_2 or NUMBER_1 == NUMBER_3 or NUMBER_2 == NUMBER_3:
            print('Вы ввели  два равных числа')
        else:
            print(f'Среднее число = {NUMBER_3}')
        break
    except ValueError:
        print('Ошибка ввода. Введите число.')
