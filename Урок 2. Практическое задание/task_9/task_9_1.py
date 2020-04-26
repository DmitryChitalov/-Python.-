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

while True:
    MAX_SUM = 0
    MAX_SUM_NUMBER = 0
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
                    NUM = int(input(f'Введите {i} число:\r\n'))
                    if NUM < 0:
                        raise IOError
                except (ValueError, TypeError, IOError):
                    print(f'Ошибка ввода  {i} числа.\r\n'
                          'Необходимо ввести целое положительное число.')
                else:
                    NUM_UNIT = NUM
                    SUM_NUMBER = 0
                    while True:
                        NUM_UNIT, BUFFER_NUM = NUM_UNIT // 10, NUM_UNIT % 10
                        SUM_NUMBER += BUFFER_NUM
                        if NUM_UNIT == 0:
                            if SUM_NUMBER > MAX_SUM:
                                MAX_SUM = SUM_NUMBER
                                MAX_SUM_NUMBER = NUM

                            break
                    break
    print(f"Наибольшее число по сумме цифр: {MAX_SUM_NUMBER}, сумма его цифр: {MAX_SUM}.")
    break
