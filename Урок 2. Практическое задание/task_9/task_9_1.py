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
NUMBER = 0
SUM = 0


def count_sum(value):
    global SUM, NUMBER
    result = 0
    tmp = value

    while tmp > 0:
        result += tmp % 10
        tmp = tmp // 10

    if result > SUM:
        SUM = result
        NUMBER = value


NUMBERS = int(input("Введите количество чисел:\n"))

for I in range(1, NUMBERS + 1):
    VALUE = int(input("Введите очередное число: "))
    count_sum(VALUE)

print(f"Наибольшее число по сумме цифр: {NUMBER}, сумма его цифр: {SUM}")
