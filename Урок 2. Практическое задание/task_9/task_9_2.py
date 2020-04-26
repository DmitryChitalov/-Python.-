"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def recursion(COUNT, ITER=1, NUMB_1=0):
    if COUNT == 0:
        return print(f'Максимальное из введенных: {NUMB_1}')
    else:
        NUMB_2 = int(input(f'Введите число №{ITER}: '))
        return (recursion(COUNT - 1, ITER + 1, NUMB_2)) if NUMB_2 > NUMB_1 else (recursion(COUNT - 1, ITER + 1, NUMB_1))

COUNT_NUMB = int(input('Введите количество чисел: '))
recursion(COUNT_NUMB)