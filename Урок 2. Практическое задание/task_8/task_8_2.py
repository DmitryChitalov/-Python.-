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


def rec_digit_count(number, digit, count=0):
    """Recursive counter of digits in namber"""
    count += 1 if number % 10 == digit else 0
    if number // 10:
        return count + rec_digit_count(number // 10, digit)
    return count


def rec_nums_count(quantity, digit):
    """Recursive coutner of digits in several numbers"""
    if quantity:
        num = abs(int(input(f'Введите число: ')))
        return rec_digit_count(num, digit) + \
            rec_nums_count(quantity - 1, digit)
    return 0


try:
    QUANTITY = int(input('Сколько будет чисел? - '))
    if QUANTITY <= 0:
        raise ValueError('Отрицательное или нулевое количество.')
    DIGIT_TO_COUNT = int(input('Какую цифру считать? - '))
    if DIGIT_TO_COUNT < 0 or DIGIT_TO_COUNT // 10 != 0:
        raise ValueError('Цифра - это число от "0" до "9"!')

    COUNT = rec_nums_count(QUANTITY, DIGIT_TO_COUNT)

    print(f'Во введенных числах {COUNT} цифр "{DIGIT_TO_COUNT}"')
except ValueError as err:
    print(f'Ошибка ввода, ошибка: {err}')
