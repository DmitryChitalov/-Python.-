"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

def cycle_method(NUM):

    a = 0
    for i in range(1, NUM + 1):
        a += i
        b = NUM * (NUM + 1) // 2
    print(f"Равенство { a == b}")

try:
    NUM = int(input("Введите число: "))
    cycle_method(NUM)
except ValueError:
    print("Введено не число")