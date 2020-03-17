"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def cycle() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ """
    try:
        n_value = abs(int(input('Введите n: ').strip()))
        sum_value = 0
        for i in range(1, n_value + 1):
            sum_value += i
        mult_value = int(n_value * (n_value + 1) / 2)
        print(f'1+2+...+n = {sum_value}')
        print(f'(n+1)/2 = {mult_value}')
        print(f'Равенство выполняется?: {sum_value == mult_value}')
    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    cycle()
