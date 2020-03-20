"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
    COUNT_ITER = int(input('Введите количество элементов из ряда: '))
    NUM = 1
    SUM = 0

    while COUNT_ITER > 0:
        SUM = SUM + NUM
        NUM /= -2
        COUNT_ITER -= 1

    print(f'Сумма элементов ряда: {SUM}')
except ValueError:
    print('Необходимо вводить число.')
