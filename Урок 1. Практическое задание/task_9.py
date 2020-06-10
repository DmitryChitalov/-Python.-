"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

int_1 = int(input('Enter first number: '))
int_2 = int(input('Enter second number: '))
int_3 = int(input('Enter third number: '))

if int_1 > int_2:
    if int_2 > int_3:
        print(f'Average number is {int_2}   marker 1')
    else:
        print(f'Average number is {int_1}   marker 2')
elif int_2 > int_1:
    if int_1 > int_3:
        print(f'Average number is {int_1}   marker 3')
    else:
        print(f'Average number is {int_2}   marker 4')
elif int_3 > int_1:
    if int_1 > int_2:
        print(f'Average number is {int_1}   marker 5')
    else:
        print(f'Average number is {int_2}   marker 6')
elif int_3 > int_2:
    if int_2 > int_1:
        print(f'Average number is {int_2}   marker 7')
    else:
        print(f'Average number is {int_1}   marker 8')
elif int_2 > int_3:
    if int_3 > int_1:
        print(f'Average number is {int_3}   marker 9')
    else:
        print(f'Average number is {int_1}   marker 10')

# NOT COMPLETED TASK



