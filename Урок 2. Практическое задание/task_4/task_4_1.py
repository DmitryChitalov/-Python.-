"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def cycle_method(n_count):

    numb = 1
    i = 0
    common_sum = 0
    while i < n_count:
        common_sum += numb
        numb = numb / 2 * -1
        i += 1
    return common_sum


try:
    N_COUNT = int(input('Введите количество элементов: '))
    print(f'Количество элемнтов - {N_COUNT}, их сумма: {cycle_method(N_COUNT)}')
except ValueError:
    print('Введите число!')
