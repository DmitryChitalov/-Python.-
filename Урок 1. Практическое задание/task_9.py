"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
first_num = input('введите первое число: ')
sec_num = input('введите второе число: ')
third_num = input('введите третье число: ')
if sec_num < first_num < third_num or third_num < first_num < sec_num:
    print(f'Среднее: {first_num}')
elif first_num < sec_num < third_num or third_num < sec_num < first_num:
    print(f'Среднее: {sec_num}')
else:
    print(f'Среднее: {third_num}')