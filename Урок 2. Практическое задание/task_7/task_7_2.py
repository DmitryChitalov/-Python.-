"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion(r_n) -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ """
    if r_n <= 0:
        return r_n
    return r_n + recursion(r_n - 1)


if __name__ == "__main__":
    try:
        N_VALUE = abs(int(input('Введите n: ').strip()))
        SUM_VALUE = recursion(N_VALUE)
        MULT_VALUE = int(N_VALUE * (N_VALUE + 1) / 2)
        print(f'1+2+...+n = {SUM_VALUE}')
        print(f'(n+1)/2 = {MULT_VALUE}')
        print(f'Равенство выполняется?: {SUM_VALUE == MULT_VALUE}')
    except ValueError:
        print('Недопустимое значение. Выходим')
