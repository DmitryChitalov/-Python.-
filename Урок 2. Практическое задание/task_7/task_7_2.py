"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def natural(NUMBER):
    assert NUMBER < 999, 'Большое число'
    if NUMBER == 1:
        return NUMBER
    sum_num = NUMBER + natural(NUMBER - 1)
    return sum_num


NUMBER = int(input('Введите любое натуральное число: '))

LEFT = natural(NUMBER)
RIGHT = NUMBER * (NUMBER + 1) // 2

print(f'LEFT = {LEFT}\n'
      f'RIGHT = {RIGHT}\n')
print('Верно' if LEFT == RIGHT else 'Не верно')
