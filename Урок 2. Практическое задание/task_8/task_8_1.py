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


def recurs(num):
    global summ
    if num // 10 == 0:
        if num == f:
            summ += 1
        else:
            return
    elif num % 10 == f:
        summ += 1
        return recurs(num // 10)
    else:
        return recurs(num // 10)


while True:
    summ = 0
    a = 1
    print('Для завершения программы введите 0')
    try:
        n = int(input('Сколько будет чисел?  '))
    except Exception as e:
        print('Вы должны ввести натуральное число!')
        continue

    if n == 0:
        print('Программа завершена!')
        break
    try:
        f = int(input('Какую цифру считать?  '))
    except Exception as e:
        print('Вы должны ввести натуральное число!')
        continue

    while n != 0:
        try:
            num = int(input(f'Введите число {a}: '))
            a += 1
            n -= 1
            if num // 10 == 0 and num == f:
                summ += 1
            else:
                recurs(num)
        except Exception as e:
            print('Вы должны ввести натуральное число!')

    print(summ)

