"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""
STEPS = int(input('Введите количество элементов: '))


def sum_steps(steps, unit=1, count=0, nums=0):
    if steps == 0:
        print(f'Количество элементов - {nums}, их сумма - {count}')
        return
    nums += 1
    count += unit
    unit /= -2
    sum_steps(steps - 1, unit, count, nums)


sum_steps(STEPS)
