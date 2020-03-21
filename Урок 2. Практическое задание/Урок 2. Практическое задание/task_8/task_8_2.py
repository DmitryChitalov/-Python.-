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
def new_func(QUALITY_OF_NUMBERS, NUMBER_TO_SCORE, NUMBERS, count):
    try:
        if QUALITY_OF_NUMBERS >= 0 and NUMBER_TO_SCORE >= 0:
            if NUMBERS > 0:
                if NUMBERS % 10 == NUMBER_TO_SCORE:
                    count += 1
                NUMBERS //= 10
                return new_func(QUALITY_OF_NUMBERS, NUMBER_TO_SCORE, NUMBERS, count)
            print(f'Цифра {NUMBER_TO_SCORE} встречается {count} раз')
        else:
            raise ValueError
    except ValueError:
        print('Некорректное значение. Введите натуральное число')

QUALITY_OF_NUMBERS = int(input('Сколько будет чисел? - '))
NUMBER_TO_SCORE = int(input('Какую цифру считать?'))
for el in range(1, QUALITY_OF_NUMBERS + 1):
    NUMBERS = int(input("Число " + str(el) + ": "))
new_func(QUALITY_OF_NUMBERS, NUMBER_TO_SCORE, NUMBERS, count=0)
