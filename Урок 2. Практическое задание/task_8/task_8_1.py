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

while True:
    try:
        COUNT_NUMBERS = int(input('Введите количество чисел в последовательности:\r\n'))
        if COUNT_NUMBERS < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода. Необходимо ввести целое положительное число.')
    else:
        while True:
            try:
                NUMBER = int(input('Введите цифру, которую необходимо подсчитать (от 0 до 9):\r\n'))
                if NUMBER > 9:
                    raise IOError
            except IOError:
                print('Ошибка ввода. Цифра не может быть больше 9 и отрицательной.')
            except (ValueError, TypeError):
                print('Ошибка ввода. Необходимо ввести целое положительное число не более 9.')
            else:
                COUNT_NUMBER = 0
                for i in range(1, COUNT_NUMBERS + 1):
                    while True:
                        try:
                            NUM = int(input(f'Введите {i} число:\r\n'))
                            if NUM < 0:
                                raise IOError
                        except (ValueError, TypeError, IOError):
                            print('Ошибка ввода последовательности чисел.\r\n'
                                  'Необходимо ввести целое положительное число.')
                        else:
                            while True:
                                NUM, BUFFER_NUM = NUM // 10, NUM % 10
                                if BUFFER_NUM == NUMBER:
                                    COUNT_NUMBER += 1
                                if NUM == 0:
                                    break
                            break
                break
        print(f"Было введено {COUNT_NUMBER} цифр '{NUMBER}'.")
        break
