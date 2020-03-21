"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    NUMBER = int(input('Введите количество чисел:'))
    if NUMBER > 0:
        MAX_SUMM = 0
        MAX_NUMBER = 0
        COUNT = 0
        while NUMBER != COUNT:
            NEXT_NUMBER = int(input('Введите очередное число:'))
            if NEXT_NUMBER >= 0:
                MAX_NEXT_NUMBER = NEXT_NUMBER
                SUMM_NUMBER = 0
                COUNT += 1
                while NEXT_NUMBER > 0:
                    SUMM_NUMBER += NEXT_NUMBER %10
                    NEXT_NUMBER //= 10
                if SUMM_NUMBER > MAX_SUMM:
                    MAX_SUMM = SUMM_NUMBER
                    MAX_NUMBER = MAX_NEXT_NUMBER
            else:
                raise ValueError
        print(f'Наибольшее число по сумме цифр : {MAX_NUMBER}, сумма цифр {MAX_SUMM}')
    else:
        raise ValueError
except ValueError:
    print('Некорректное значение.Введите натуральное число')
