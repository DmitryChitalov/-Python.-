"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def calc_sum(number, sum_number, next_element, str_numbers):
    if number == 0:
        return str_numbers, sum_number
    else:
        str_numbers = ', '.join((str_numbers, str(next_element / -2)))
        return calc_sum(number - 1, sum_number + next_element, next_element / -2, str_numbers)


while True:
    try:
        # Запрос на ввод числа
        NUMBER = int(input('Введите целое положительное число:\r\n'))
        # Проверка числа что оно не отрицательное
        if NUMBER <= 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода. Требуется ввести положительное целое число.')
    else:
        # Строка с элементами ряда
        STR_NUMBERS = '1'
        # Вывод результата
        STR_NUMBERS, SUM = calc_sum(NUMBER, 0, 1, STR_NUMBERS)
        # print(f'Сумма {NUMBER} элементов ряда чисел {calc_sum(NUMBER, 0, 1, STR_NUMBERS)[0]} ='
        # f' {calc_sum(NUMBER, 0, 1, STR_NUMBERS)[1]}')
        print(f'Сумма {NUMBER} элементов ряда чисел {STR_NUMBERS} =  {SUM}')
        break
