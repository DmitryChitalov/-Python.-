"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
n = int(input("Введите количество слагаемых:  "))
S = 0
for i in range(1, n+1):
    S = S + i
S1 = n * (n+1)/2
if S == S1:
    print("Тождество верно.")
else:
    print("Тождество не верно.")