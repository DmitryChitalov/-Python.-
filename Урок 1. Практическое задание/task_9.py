"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
A = int(input('Enter the first number: '))
B = int(input('Enter the second number: '))
C = int(input('Enter the third number: '))

# Checking if numbers are equal, then find the middle with multiplication
if A == B or A == C or B == C:
    print('No middle')
else:
    if (B - A) * (A - C) > 0:
        print(f'The middle is {A}')
    elif (A - B) * (B - C) > 0:
        print(f'The middle is {B}')
    else:
        print(f'The middle is {C}')

# Checking if numbers are not equal, then find the middle with comparing
if A != B and A != C and B != C:
    if A > B > C or C > B > A:
        print(f'The middle is {B}')
    elif B > A > C or C > A > B:
        print(f'The middle is {A}')
    else:
        print(f'The middle is {C}')
else:
    print('No middle')
