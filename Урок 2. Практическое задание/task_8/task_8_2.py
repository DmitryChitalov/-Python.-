"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion_digit_quantity(r_input, r_number, r_quantity):
    """ Рекурсивный поиск цифры в числе """
    if r_input <= 0:
        return r_quantity

    if r_input % 10 == r_number:
        r_quantity += 1
    return recursion_digit_quantity(r_input // 10, r_number, r_quantity)


def recursion_input(r_iteration, r_count, r_number, r_quantity=0) -> int:
    """ Рекурсивный запрос числа """

    if r_iteration > r_count:
        return r_quantity
    try:
        user_input = abs(int(input(f'Число {r_iteration}: ')))
        r_quantity = recursion_digit_quantity(user_input, r_number, r_quantity)
        return recursion_input(r_iteration + 1, r_count, r_number, r_quantity)

    except ValueError:
        print('Недопустимое значение.')
        return recursion_input(r_iteration + 1, r_count, r_number, r_quantity)


if __name__ == "__main__":
    try:
        COUNT = abs(int(input('Сколько будет чисел? : ')))
        NUMBER = abs(int(input('Какую цифру считать? : ')))

        QUANTITY = recursion_input(1, COUNT, NUMBER)

        print(f'Было введено {QUANTITY} цифр "{NUMBER}"')
    except ValueError:
        print('Недопустимое значение. Выходим')
