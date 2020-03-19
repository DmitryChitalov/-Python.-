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


def num_count_digit(num):
    """
    Считаем количество повторений выбранной цифры в числе
    """
    global NEED_NUMS_COUNT, DIGIT
    if num != 0:
        if num % 10 == DIGIT:
            NEED_NUMS_COUNT += 1
        num_count_digit(num // 10)


def count_digit(n):
    """
    Реализация через рекурсию
    """
    global DIGIT, NEED_NUMS_COUNT, COUNT_NUMS
    if n == 0:
        print(f'Было введено {NEED_NUMS_COUNT} цифр {DIGIT}')
    else:
        num = int(input(f'Введите число {COUNT_NUMS - n + 1}: '))
        num_count_digit(num)
        count_digit(n - 1)


if __name__ == "__main__":
    NEED_NUMS_COUNT = 0
    try:
        COUNT_NUMS = int(input("Введите количество вводимых чисел: "))
        if COUNT_NUMS <= 0:
            print ('Число должно быть положительным')
        else:
            DIGIT = int(input("Введите цифру, которую будем считать: "))
            print(count_digit(COUNT_NUMS))
    except ValueError:
        print("Ошибка ввода значения")
