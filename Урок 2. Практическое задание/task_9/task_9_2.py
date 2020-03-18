"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
NUMBER = 0
SUM = 0


def recursive_count_sum(value, sum=0):

    if value == 0:
        return sum
    else:
        return recursive_count_sum(value // 10, sum + value % 10)


def recursive_max_method(n):
    global NUMBER, SUM

    if n == 0:
        print(f"Наибольшее число по сумме цифр: {NUMBER}, сумма его цифр: {SUM}")
    else:
        value = int(input("Введите очередное число: "))
        current_sum = recursive_count_sum(value)
        if current_sum > SUM:
            SUM = current_sum
            NUMBER = value
        recursive_max_method(n-1)


NUMBERS = int(input("Введите количество чисел:\n"))

recursive_max_method(NUMBERS)