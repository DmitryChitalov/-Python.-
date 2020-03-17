"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def cycle_sum() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ """
    sum_value = 0
    start_value = 1
    i = 1
    try:
        n_value = abs(int(input('Введите количество элементов: ').strip()))
        while i <= n_value:
            if i % 2 == 0:
                sum_value = sum_value - start_value
            else:
                sum_value = sum_value + start_value
            start_value /= 2
            i += 1
        print(f'Количество элементов - {n_value}, их сумма - {sum_value}')
    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    cycle_sum()
