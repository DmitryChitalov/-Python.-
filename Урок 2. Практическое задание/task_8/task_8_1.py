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


def counter_number():
    try:
        count_number = int(input('Введите количество чисел: '))
        check_number = int(input('Какую цифру считать:  '))
        counter = 0
        for i in range(1, count_number + 1):
            user_number = int(input(f'Введите {i} число: '))
            while user_number > 0:
                if user_number % 10 == check_number:
                    counter += 1
                user_number //= 10
        print(f'Было введено {counter} цифр "{check_number}"')
    except ValueError:
        print('Вводите корректные данные')
        counter_number()


counter_number()
