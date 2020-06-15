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


def natural_numbers(count, max_num=0, max_sum_num=0):
    """Наибольшее по сумме цифр
    (для усложнения сперва делалась рекурсия, тут её быстрая переделка под цикл)

    count - количество чисел
    max_num - число с максимальной суммой цифр
    max_sum_num - максимальная сумма цифр
    """
    while True:
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
        count -= 1


try:
    COUNT = int(input("Введите количество чисел: "))

    print(natural_numbers(COUNT))
except ValueError:
    print("Необходимо вводить только числа!")
