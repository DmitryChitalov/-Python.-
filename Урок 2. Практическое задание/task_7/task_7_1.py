"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
def fun(number):

    k = 0
    for i in range(1, number + 1):
        k += i
        f = number * (number + 1) // 2
    print(f"{k == f}")


try:
    NUMBER = int(input("Введите число: "))
    fun(NUMBER)
except ValueError:
    print("Вы ввели некорректные данные")

