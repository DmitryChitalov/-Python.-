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

def sum_num(enter_num):
    """
    Функция обрабатывает число enter_num передавая в качестве результата сумму цифр числа.

    :param enter_num: введённое число
    :return: сумма цифр введённого числа
    """
    num = enter_num % 10
    enter_num = enter_num // 10
    if enter_num > 0:
        all_sum = sum_num(enter_num)
        return all_sum + num
    return num

def entering_numbers(val, step=1, max_num=0, max_num_sum=0):
    """
    Функция entering_numbers запрашивает у пользователя ввод чисел,
    рекурсивно вызывая себя.

    Для подсчёта суммы цифр, entering_numbers использует функцию sum_num(enter_num).
    :param val: количество цифр, которые функция будет сравнивать
    :param step: шаг функции (нужен только для отображения пользователю
    :param max_num: хранит число с максимальной суммой цифр
    :param max_num_sum: Хранит сумму цифр числа max_num
    :return: Число с максимальной суммой цифр
    """
    try:
        if val != 0:
            while True:
                enter_num = int(input(f'Число {step}: '))
                if enter_num <= 0:
                    print('Необходимо вводить число - больше нуля!')
                    continue
                break
            enter_num_sum = sum_num(enter_num)
            if enter_num_sum > max_num_sum:
                max_num = enter_num
                max_num_sum = enter_num_sum
            max_num, max_num_sum = entering_numbers(val - 1, step + 1, max_num, max_num_sum)
        return max_num, max_num_sum
    except ValueError:
        print('Необходимо вводить числа!')

try:
    while True:
        COUNT_NUM = int(input('Сколько будет чисел? - '))
        if COUNT_NUM <= 0:
            print('Необходимо вводить число - больше нуля!')
            continue
        break
    MAX_NUM, MAX_NUM_SUM = entering_numbers(COUNT_NUM)
    print(f'Наибольшее число по сумме цифр: {MAX_NUM}, сумма его цифр: {MAX_NUM_SUM}')
except ValueError:
    print('Необходимо вводить числа!')
