"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
# ожидаем ввод пользователя
USR_A = int(input('Введите первое число: '))
USR_B = int(input('Введите второе число: '))
USR_C = int(input('Введите третье число: '))

# проверяем что число b является средним, т.е. меньше a и больше c, либо наоборот
if (USR_A < USR_B < USR_C) or (USR_C < USR_B < USR_A):
    print(f'Среднее: {USR_B}')
# если предыдущее условие ложное, то делаем аналогичную проверку для числа a
elif (USR_B < USR_A < USR_C) or (USR_C < USR_A < USR_B):
    print(f'Среднее: {USR_A}')
# проверяем не равны ли первые два числа друг другу, а также меньше или равны ли они числу c
elif (USR_B == USR_A) and (USR_B <= USR_C):
    print(f'Среднее: {USR_B}')
# если оба предыдущих числа не являются средними, значит средним является число c
else:
    print(f'Среднее: {USR_C}')
