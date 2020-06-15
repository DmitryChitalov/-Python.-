"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def equality_theorem(num, result=0):
    """Возвращаем 1+2+...+n
    (для усложнения сперва делалась рекурсия, тут её быстрая переделка под цикл)

    num - n - высшее натуральное число
    result - сумма чисел
    """

    while num > 0:
        result += num
        num -= 1
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
