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
try:
    NUMBER = int(input('Enter a number : '))
    REVERSE = 0
    if NUMBER > 0:
        while NUMBER != 0:
            REVERSE *= 10
            REVERSE += NUMBER % 10
            NUMBER = NUMBER // 10
        print(REVERSE)
    else:
        raise ValueError
except ValueError:
    print('Incorrect number.')

