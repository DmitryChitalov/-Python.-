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


def natural_numbers(count, max_num=0, max_sum_num=0):
    """Наибольшее по сумме цифр

    count - количество чисел
    max_num - число с максимальной суммой цифр
    max_sum_num - максимальная сумма цифр
    """
    if not count:
        return f"Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum_num}"
    user_number = int(input("Введите число: "))
    temporary_number = user_number
    sum_user_number = 0
    while temporary_number > 0:
        sum_user_number += temporary_number % 10
        temporary_number //= 10
    if sum_user_number > max_sum_num:
        max_num = user_number
        max_sum_num = sum_user_number
    return natural_numbers(count - 1, max_num, max_sum_num)


try:
    COUNT = int(input("Введите количество чисел: "))

    print(natural_numbers(COUNT))
except ValueError:
    print("Необходимо вводить только числа!")
