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


def get_max(digit_sum, max_sum, max_num, curr_count, count_nums):
    """
    Реализация через цикл
    """
    while curr_count < count_nums:
        num = int(input("Введите число: "))
        copy_num = num
        while num > 0:
            digit_sum += num % 10
            num //= 10
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = copy_num
        digit_sum = 0
        curr_count += 1

    return f'Наибольшее число по сумме цифр {max_num}, сумма его цифр: {max_sum}'


if __name__ == "__main__":
    CURR_COUNT = 0
    DIGIT_SUM = 0
    MAX_SUM = 0
    MAX_NUM = 0
    try:
        COUNT_NUMS = int(input("Введите количество вводимых чисел: "))
        if COUNT_NUMS <= 0:
            print("Число должно быть положительным")
        else:
            print(get_max(DIGIT_SUM, MAX_SUM, MAX_NUM, CURR_COUNT, COUNT_NUMS))
    except ValueError:
        print("Ошибка ввода значения")
