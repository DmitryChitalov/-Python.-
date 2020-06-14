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


def user_number_input():
    user_number_in = int(input('Введите количество чисел: '))

    def sum_number(user_number, max_sum_number=0, maximum_number=0):
        if user_number == 0:
            return print(f'Максимальная сумма введенных чисел {max_sum_number}, '
                         f'это число {maximum_number}')

        user_input = int(input('Введите число: '))
        max_number = user_input
        max_sum = 0
        while user_input > 0:
            max_sum += user_input % 10
            user_input //= 10
            if max_sum > max_sum_number:
                max_sum_number = max_sum
                maximum_number = max_number
        user_number -= 1
        return sum_number(user_number, max_sum_number, maximum_number)

    sum_number(user_number_in)


user_number_input()
