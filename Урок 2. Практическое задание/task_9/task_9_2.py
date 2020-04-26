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

def max_sum_number(n, max_sum, max_number):
    if n == 0:
        return print(f"Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_sum}.")
    number = int(input("Введите число: "))
    sum = 0
    m = number
    while m > 0:
        sum += m % 10
        m //= 10
    if max_sum < sum:
        max_sum = sum
        max_number = number
    return max_sum_number(n-1, max_sum, max_number)

try:
    n = int(input("Введите количество чисел:  "))
    max_sum_number(n, 0, 0)
except ValueError:
    print("Неправильный ввод данных.")
