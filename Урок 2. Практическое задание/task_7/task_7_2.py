"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_sum(num):
    """Recursion sum. Return sum 1+2+...+num"""
    return num + recursion_sum(num - 1) if num > 1 else 1


try:
    N = int(input('Введите число: '))
    if N < 0:
        raise ValueError('Число должно быть положительным.')
    SUM = int(N * (N + 1) / 2)
    if SUM == recursion_sum(N):
        print(f'Выражение 1+2+...+n = n(n+1)/2 верно для n = {N}!')
    else:
        print(f'С числом {N} что-то пошло не так!')
except ValueError as err:
    print(f'Ошибка ввода. Попробуйте еще раз. Ошибка: {err}')
