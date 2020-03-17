"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_sum() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ """

    def recursion(r_n, start):
        if r_n == 1:
            return start
        return start + recursion(r_n - 1, -start / 2)

    try:
        n_value = abs(int(input('Введите количество элементов: ').strip()))
        sum_value = recursion(n_value, 1)

        print(f'Количество элементов - {n_value}, их сумма - {sum_value}')
    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    recursion_sum()
