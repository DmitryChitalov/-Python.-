"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_sum_numbers(number):
    return 1 if number == 1 else number + recursion_sum_numbers(number - 1)


while True:
    try:
        NUMBER = int(input('Введите натуральное число:\r\n'))
        if NUMBER < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода. Необходимо ввести целое положительное число.')
    else:
        SUM = recursion_sum_numbers(NUMBER)
        SUM_FORMULA = NUMBER * (NUMBER + 1) / 2
        print(f'Для множества натуральных чисел 1 + ... + {NUMBER} сумма ряда = {SUM}.\r\n'
              f'Сумма данного ряда по формуле N(N+1)/2 = {SUM_FORMULA:.0f}')
        if SUM == SUM_FORMULA:
            print('Результаты поэлементного расчета суммы ряда совпадают с расчетом по формуле.\r\n'
                  'Следовательно, равенство 1 + 2 + ... + n = n(n + 1) / 2 выполняется')
        else:
            print('Результаты поэлементного расчета суммы ряда не совпадают с расчетом по формуле.\r\n'
                  'Следовательно, равенство 1 + 2 + ... + n = n(n + 1) / 2 не выполняется.')
        break
