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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    QUALITY_OF_NUMBERS = int(input('Сколько будет чисел? - '))
    NUMBER_TO_SCORE = int(input('Какую цифру считать?'))
    if QUALITY_OF_NUMBERS >= 0 and NUMBER_TO_SCORE >= 0:
        COUNT = 0
        for el in range(1, QUALITY_OF_NUMBERS +1):
            NUMBERS = int(input("Число " + str(el) + ": "))
            while NUMBERS > 0:
                if NUMBERS %10 == NUMBER_TO_SCORE:
                    COUNT += 1
                NUMBERS = NUMBERS // 10
        print(f'Цифра {NUMBER_TO_SCORE} встречается {COUNT}  раз')
    else:
        raise ValueError
except ValueError:
    print('Некорректное значение. Введите натуральное число')
