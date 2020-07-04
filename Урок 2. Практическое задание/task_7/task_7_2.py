"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def checkin(n,equality1 = 0, equality2 = 1 ):
    if equality1 == equality2:
        return print(f"{equality1} = {equality2}")
    elif equality1 < equality2 :
        checkin(n, equality1+1, n * (n + 1) // 2)


try:
    n = int(input("Введите число n: "))
    checkin(n)
except ValueError:
    print('Вы допустили ошибку при вводе значения. Попробуйте еще раз: ')
