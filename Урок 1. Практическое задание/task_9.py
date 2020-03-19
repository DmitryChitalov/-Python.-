"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
ER_STRING = 'Ошибка ввода!'
try:
    num_a = int(input('Введите первое число: '))
    num_b = int(input('Введите второе число: '))
    num_c = int(input('Введите третье число: '))
    if num_a == num_b or num_b == num_c or num_a == num_c:
        print('Не допустимы повторяющиеся числа!')
        print(ER_STRING)
    else:
        if num_b > num_a and num_b < num_c or num_b < num_a and num_b > num_c:
            num_mid = num_b
        elif num_a > num_b and num_a < num_c or num_a < num_b and num_a > num_c:
            num_mid = num_a
        elif num_c > num_a and num_c < num_b or num_c < num_a and num_c > num_b:
            num_mid = num_c
        print('среднее число %d' %(num_mid))
except:
    print(ER_STRING)