"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
first_int = int(input('введите первое число: '))
second_int = int(input('введите второе число: '))
third_int = int(input('введите третье число: '))

if first_int > second_int:
    if second_int > third_int:
        print('третье число среднее')
    else:
        print('второе число среднее')
else:
    if second_int > third_int:
        if third_int < first_int:
            print('третье число среднее')
    else:
        print('первое число среднее')
