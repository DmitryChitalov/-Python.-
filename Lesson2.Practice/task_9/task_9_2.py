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


def get_sum(num, max_sum):
    """
    Вычисление суммы цифр числа
    """
    if num == 0:
        return max_sum
    max_sum = max_sum + num % 10
    return get_sum(num // 10, max_sum)


def get_max(count_nums, max_sum=0, max_num=0):
    """
    Получение числа с большей суммой цифр
    """
    if count_nums <= 0:
        return max_num, max_sum
    try:
        user_num = abs(int(input("Введите число: ")))
        digit = get_sum(user_num, 0)
        if digit > max_sum:
            max_sum = digit
            max_num = user_num
        return get_max(count_nums - 1, max_sum, max_num)
    except ValueError:
        print("Ошибка ввода значения")


if __name__ == "__main__":
    try:
        COUNT_NUMS = int(input("Введите количество чисел: "))
        if COUNT_NUMS < 0:
            print("Количество чисел должно быть неотрицательным")
        else:
            MAX_NUM, MAX_SUM = get_max(COUNT_NUMS)
            print(
                f'Наибольшее число по сумме цифр: {MAX_NUM}, сумма его цифр: {MAX_SUM}')
    except ValueError:
        print("Ошибка ввода значения")
