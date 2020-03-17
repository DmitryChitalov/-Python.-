"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def cycle_reverse() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ """

    try:
        value = int(input('Введите число: ').strip())
        invert_value = 0

        if value <= 0:
            print('Недопустимое значение. Выходим')
        else:
            while value > 0:
                if 1 <= value <= 9:
                    invert_value = (invert_value + value % 10)
                    value = value // 10
                else:
                    invert_value = (invert_value + value % 10) * 10
                    value = value // 10

            print(f'Перевернутое число: {invert_value}')

    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    cycle_reverse()
