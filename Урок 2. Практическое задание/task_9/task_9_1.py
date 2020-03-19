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
    try:
        NUMBER1 = int(input(f'Введите количество чисел: '))
        ANSWER = 0
        NUMBER_FOR_ANSWER = 0
        for i in range(NUMBER1):
            MY_SUM = 0
            SPAM = int(input('Введите очередное число: '))
            EGG = SPAM
            if SPAM // 10 == 0:
                if ANSWER < SPAM:
                    ANSWER = SPAM
                    NUMBER_FOR_ANSWER = SPAM
            while SPAM > 0:
                MY_SUM += SPAM % 10
                SPAM = SPAM // 10
            if ANSWER < MY_SUM:
                ANSWER = MY_SUM
                NUMBER_FOR_ANSWER = EGG
        print(f'Наибольшее число по сумме цифр: {NUMBER_FOR_ANSWER}, сумма его цифр: {ANSWER}')
        break
    except ValueError:
        print(f'Ошибка ввода! ')
