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
        NUMBER1 = int(input(f"How many integers will be? "))
        ANSWER = 0
        NUMBER_FOR_ANSWER = 0
        for i in range(NUMBER1):
            MY_SUM = 0
            SPAM = int(input("Input another integer "))
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
        print(
            f'Integer {NUMBER_FOR_ANSWER} is max, sum of his integers is: {ANSWER}')
        break
    except ValueError:
        print(f'Error ')
