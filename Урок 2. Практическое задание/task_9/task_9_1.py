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


def cycle_sum_numbers() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ """
    try:
        numbers_quantity = abs(
            int(input('Введите количество чисел: ').strip()))
        max_number = 0
        max_sum = 0
        for _ in range(numbers_quantity):
            inputed_number = abs(
                int(input('Введите очередное число: ').strip())
            )
            current_sum = 0
            current_number = inputed_number
            while current_number > 0:
                current_sum += current_number % 10
                current_number = current_number // 10
            if current_sum > max_sum:
                max_sum = current_sum
                max_number = inputed_number

        print(
            f'Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_sum}')

    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    cycle_sum_numbers()

# В этой реализации не исключен вариант что все числа могут быть равны по сумме цифр
# Введите количество чисел: 3
# Введите очередное число: 555
# Введите очередное число: 78
# Введите очередное число: 87
# Наибольшее число по сумме цифр: 555, сумма его цифр: 15
