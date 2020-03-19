"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def rec_prog_sum(num, f_value, den, summ=0):
    """
    Recursion. Sum of geometric progression.
    Get number, first value, denominator, sum.
    Return sum of geometric progression.
    """
    summ += f_value
    return rec_prog_sum(num - 1, f_value * den, den, summ) if num > 1 else summ


FIRST_VALUE = 1  # Начальное значение прогрессии
DENOM = -0.5  # Знаменатель прогрессии

try:
    NUM = int(input('Введите количество элементов: '))
    if NUM > 0:
        print(f'Количество элементов - {NUM}, их сумма - '
              f'{rec_prog_sum(NUM, FIRST_VALUE, DENOM)}')

        # Для проверки сумма этой геометрической прогрессии:
        print(f'Проверка = {FIRST_VALUE * (DENOM ** NUM - 1) / (DENOM - 1)}')
    else:
        raise ValueError('Число меньше или равно нулю, повторите ввод.')
except ValueError as err:
    print(f'Ошибка ввода: {err}')
