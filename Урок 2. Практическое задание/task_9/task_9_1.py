"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys

try:
    AMOUNT = int(input("Введите количество чисел: "))
except ValueError:
    print("Некорректные  данные, программа завершена")
    sys.exit()

if AMOUNT < 1:
    print("Количество вводимых чисел не должно быть меньше 1, программа завершена")
    sys.exit()

RESULT = 0
RESULT_SUM = 0

for i in range(AMOUNT):

    try:
        NUMBER = int(input(f"Введите очередное число:"))
    except ValueError:
        print("Некорректные  данные, программа завершена")
        sys.exit()

    RESULT_SUM_ITEM = 0
    NUMBER_ITEM = NUMBER
    while True:
        RESULT_SUM_ITEM += NUMBER_ITEM % 10
        NUMBER_ITEM = NUMBER_ITEM // 10
        if not NUMBER_ITEM:
            break

    if RESULT_SUM_ITEM > RESULT_SUM:
        RESULT = NUMBER
        RESULT_SUM = RESULT_SUM_ITEM


print(f"Наибольшее число по сумме цифр: {RESULT}, сумма его цифр: {RESULT_SUM}")
