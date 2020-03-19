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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

COUNT = 0
try:
    QUANTITY = int(input('Сколько будет чисел? - '))
    if QUANTITY < 0:
        raise ValueError('Отрицательное количество.')
    DIGIT_TO_COUNT = int(input('Какую цифру считать? - '))
    if DIGIT_TO_COUNT < 0 or DIGIT_TO_COUNT // 10 != 0:
        raise ValueError('Цифра - это число от "0" до "9"!')
    TEMP_QUANTITY = QUANTITY
    while TEMP_QUANTITY:
        NUM = abs(
            int(input(f'Введите число {QUANTITY - TEMP_QUANTITY + 1}: ')))
        TEMP_QUANTITY -= 1
        if NUM == 0:
            COUNT += 1
        while NUM:
            COUNT += 1 if NUM % 10 == DIGIT_TO_COUNT else 0
            NUM //= 10
    print(f'Во введенных числах {COUNT} цифр "{DIGIT_TO_COUNT}"')
except ValueError as err:
    print(f'Ошибка ввода, ошибка: {err}')

