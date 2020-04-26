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
def recursion(COUNT, NUMBER, ITER, RESULT):
    if COUNT == 0:
        return print(f'Было введено {RESULT} цифр {NUMBER}')
    else:
        NUMB = int(input(f'Введите число №{ITER}: '))
        while NUMB > 0:
            if NUMB % 10 == NUMBER:
                RESULT += 1
                NUMB = NUMB // 10
            else:
                NUMB = NUMB // 10
        return recursion(COUNT - 1, NUMBER, ITER + 1, RESULT)

COUNT_NUMB = int(input('Введите количество чисел: '))
NUMBER_USER = int(input('Введите количество какой цифры посчитать: '))
recursion(COUNT_NUMB, NUMBER_USER, 1, 0)