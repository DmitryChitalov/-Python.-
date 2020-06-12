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


def recursive_count_num(cnt=-1, digit=-1, number=0, res=0):
    try:
        if number != 0:
            if number % 10 == digit:
                res += 1
            return recursive_count_num(cnt, digit, number // 10, res)
        if cnt == 0:
            return res
        if cnt == -1 and digit == -1:  # Условие для первого и единственного ввода
            cnt = int(input('Введите количество чисел: '))
            digit = int(input('Какую цифру считать? '))
        if number == 0:
            number = int(input('Введите число: '))
            return recursive_count_num(cnt - 1, digit, number, res=res)
    except ValueError:
        print('Необходимо ввести число')

print(recursive_count_num())
