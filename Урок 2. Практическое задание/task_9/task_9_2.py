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


def recursion_sum_numbers(sum_number, max_sum, max_sum_number, number, num):
    if num == 0:
        if sum_number > max_sum:
            max_sum = sum_number
            max_sum_number = number
        return max_sum_number, max_sum
    else:
        return recursion_sum_numbers(sum_number + num % 10, max_sum, max_sum_number, number, num // 10)


while True:
    MAX_SUM_NUMBER = 0
    MAX_SUM = 0
    try:
        COUNT_NUMBERS = int(input('Введите количество чисел:\r\n'))
        if COUNT_NUMBERS < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода количества чисел. Необходимо ввести целое положительное число.')
    else:
        for i in range(1, COUNT_NUMBERS + 1):
            while True:
                try:
                    NUMBER = int(input(f'Введите {i} число:\r\n'))
                    if NUMBER < 0:
                        raise IOError
                except (ValueError, TypeError, IOError):
                    print(f'Ошибка ввода  {i} числа.\r\n'
                          'Необходимо ввести целое положительное число.')
                else:
                    MAX_SUM_NUMBER, MAX_SUM = recursion_sum_numbers(0, MAX_SUM, MAX_SUM_NUMBER, NUMBER, NUMBER)
                    break
    print(f"Наибольшее число по сумме цифр: {MAX_SUM_NUMBER}, сумма его цифр: {MAX_SUM}.")
    break
