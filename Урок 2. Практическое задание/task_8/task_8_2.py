"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def count_nums(enter_num, count=0):
    """
    Функция подсчета таргетных цифр в отдельном числе
    :param enter_num:
    :param count:
    :return:
    """
    if enter_num != 0:
        one_num = enter_num % 10
        if one_num == TARGET_NUM:
            count += 1
        enter_num //= 10
        next_count = count_nums(enter_num, count)
        return next_count
    return count

def entering_numbers(count_enter, count=0, step=1):
    """
    функция запроса ввода чисел, в которых производить подсчет.
    :param count_enter:
    :param count:
    :param step:
    :return:
    """
    try:
        if count_enter != 0:
            while True:
                enter_num = int(input(f'Число {step}: '))
                if enter_num <= 0:
                    print('Необходимо вводить число - больше нуля!')
                    continue
                break
            count = count + count_nums(enter_num)
            next_enter = entering_numbers(count_enter - 1, count, step + 1)
            return next_enter
        return count

    except ValueError:
        print('Необходимо вводить числа!')

try:
    COUNT_ENTER = int(input('Сколько будет чисел? - '))
    TARGET_NUM = int(input('Какую цифру считать? - '))
    print(f'Было введено {entering_numbers(COUNT_ENTER)} цифр {TARGET_NUM}')
except ValueError:
    print('Необходимо вводить числа!')
