"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

try:
    A, B, C = input('Введите 3 числа через пробел A, B и C: ').split()
    A, B, C = float(A), float(B), float(C)
    if A == B or B == C or C == A:
        raise ValueError('Числа должны быть разными.')
    if C > A > B or C < A < B:
        print('Среднее число - A')
    elif A > B > C or A < B < C:
        print('Среднее число - B')
    else:
        print('Среднее число - C')
except ValueError as err:
    print(f'Ошибка ввода: {err}')
