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


def recursion_sum_digits(number, r_sum):
    """ Рекурсивный подсчёт суммы цифр числа """
    if number <= 0:
        return r_sum
    r_sum = r_sum + number % 10
    return recursion_sum_digits(number // 10, r_sum)


def recursion_input(iteration, r_number=0, r_sum=0):
    """ Рекурсивное сравнение чисел по сумме цифр """
    if iteration <= 0:
        return r_number, r_sum

    try:
        inputed_number = abs(
            int(input('Введите очередное число: ').strip())
        )
        sum_gigit = recursion_sum_digits(inputed_number, 0)
        if sum_gigit > r_sum:
            r_number = inputed_number
            r_sum = sum_gigit

        return recursion_input(iteration - 1, r_number, r_sum)
    except ValueError:
        print('Недопустимое значение.')
        return recursion_input(iteration - 1, r_number, r_sum)


if __name__ == "__main__":
    NUMBERS_QUANTITY = abs(int(input('Введите количество чисел: ').strip()))
    MAX_NUMBER, MAX_SUM = recursion_input(NUMBERS_QUANTITY)
    print(
        f'Наибольшее число по сумме цифр: {MAX_NUMBER}, сумма его цифр: {MAX_SUM}'
    )
