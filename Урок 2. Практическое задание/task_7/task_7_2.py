"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def equality(n: int, right_part=0, left_part=1):
    if right_part == left_part:
        return 'Равенство для выполняется!'
    elif right_part < left_part:
        return equality(n, right_part + 1, n * (n + 1) // 2)


try:
    number_n = int(input('Введите любое натуральное число для n: '))
    equality(number_n)
except ValueError:
    print('Введены некорректные данные!')
