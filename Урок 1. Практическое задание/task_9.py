"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


def find_middle_num() -> None:
    """ Поиск среднего числа """
    try:
        a_val = float(input('Введите первое число: ').strip())
        b_val = float(input('Введите второе число: ').strip())
        c_val = float(input('Введите третие число: ').strip())

        if a_val == b_val or b_val == c_val or a_val == c_val:
            print('Нет среднего числа')

        elif b_val < a_val < c_val or c_val < a_val < b_val:
            print(f'Средним числом является - {a_val}')

        elif a_val < b_val < c_val or c_val < b_val < a_val:
            print(f'Средним числом является - {b_val}')

        else:
            print(f'Средним числом является - {c_val}')

    except ValueError as err:
        print('Введённое Вами значение некорректно')
        print('Ошибка: ', err)


if __name__ == "__main__":
    find_middle_num()
