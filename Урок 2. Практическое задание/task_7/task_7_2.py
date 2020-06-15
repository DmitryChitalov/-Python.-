"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def equality_theorem(num, result=0):
    """Возвращаем 1+2+...+n

    num - n - высшее натуральное число
    result - сумма чисел
    """
    result += num
    if num > 0:
        return equality_theorem(num - 1, result)
    return result


try:
    NUMBER = int(input("Введите натуральное число: "))
    if NUMBER < 0:
        raise ValueError("Вы ввели отрицательное число")

    if equality_theorem(NUMBER) == NUMBER * (NUMBER + 1) / 2:
        print(f'Теория "1+2+...+n = n(n+1)/2" верна')
    else:
        print(f'Теория "1+2+...+n = n(n+1)/2" не верна')
except ValueError as exception:
    print(f"Нужно вводить число! \n{exception}")
