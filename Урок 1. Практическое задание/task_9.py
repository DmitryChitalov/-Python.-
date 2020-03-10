"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
while True:
    try:
        print('Данная программа определит среднее число')
        VAR1 = int(input("число 1: "))
        VAR2 = int(input("число 2: "))
        VAR3 = int(input("число 3: "))
        if VAR2 < VAR1 < VAR3 or VAR3 < VAR1 < VAR2:
            print(f'Среднее число: {VAR1}')
        elif VAR1 < VAR2 < VAR3 or VAR3 < VAR2 < VAR1:
            print(f'Среднее число: {VAR2}')
        elif VAR1 == VAR2 == VAR3:
            print(f'Числа равны')
        else:
            print(f'Среднее число: {VAR3}')
        break
    except ValueError:
        print(f'Ошибка ввода')