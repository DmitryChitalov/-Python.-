"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

try:
    A = int(input("First integer: "))
    B = int(input("Second integer: "))
    C = int(input("Third integer: "))

    if B < A < C or C < A < B:
        print(f"Middle integer: {A}")
    elif A < B < C or C < B < A:
        print(f"Middle integer: {B}")
    elif A < C < B or B < C < A:
        print(f"Middle integer: {C}")
    else:
        print("Error: Input different integers")

except ValueError:
    print('Incorrect')

