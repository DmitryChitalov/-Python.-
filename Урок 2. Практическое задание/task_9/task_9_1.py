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

NUMBERS_COUNT = int(input("Введите количество чисел: "))
DIGITS_SUM = 0
MAX_DIGITS_SUM = 0
NUMBER_W_MDS = 0
for I in range(NUMBERS_COUNT):
#    MAX_DIGITS_SUM = 0
    DIGITS_SUM = 0
    NUMBER = int(input("Введите очередное число: "))
    for J in range(1, len(str(NUMBER)) + 1):
        DIGITS_SUM += (NUMBER % (10 ** J)) // (10 ** (J - 1))
#        NUMBER //= 10
    if DIGITS_SUM > MAX_DIGITS_SUM:
        MAX_DIGITS_SUM = DIGITS_SUM
        NUMBER_W_MDS = NUMBER

print("Наибольшее число по сумме цифр:", str(NUMBER_W_MDS), "сумма его цифр:", str(MAX_DIGITS_SUM))
