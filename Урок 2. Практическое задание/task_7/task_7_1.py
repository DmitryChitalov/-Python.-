"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


# Solution from teacher

def cycle_method(numb):
    s = 0
    for i in range(1, numb + 1):
        s += i
        m = numb * (numb + 1) // 2
    print(f"Equality: {s == m}")


try:
    NUMB = int(input("Enter a number: "))
    cycle_method(NUMB)
except ValueError:
    print("Wrong value. Try again")
