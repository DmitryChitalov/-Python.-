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
    NUMBER_COUNT = int(input("Сколько будет чисел?: "))
except ValueError:
    print("Введено не число")
    sys.exit()

MAX_NUMBER = 0
MAX_NUMBER_SUM = 0


for i in range(NUMBER_COUNT):
    current_number = int(input(f"Введите число {i + 1}: "))
    buffer_number = current_number
    digit_sum = 0
    while current_number != 0:
        digit_sum += current_number % 10
        current_number = current_number // 10
    if digit_sum > MAX_NUMBER_SUM:
        MAX_NUMBER_SUM = digit_sum
        MAX_NUMBER = buffer_number

print(f"Максимальная сумма цифр - {MAX_NUMBER_SUM} в числе {MAX_NUMBER}")
