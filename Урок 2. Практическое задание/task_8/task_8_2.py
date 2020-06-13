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


def user_input():
    count_number_user = int(input('Введите количество чисел: '))
    check_number_user = int(input('Какую цифру считать:  '))

    def count_numbers(count_number, check_number, cnt=1, counter=0):
        if count_number == 0:
            return print(f'Было введено {counter} цифр "{check_number}"')
        user_number = int(input(f'Введите {cnt} число: '))

        def check_user_number(user_number_check, counter_check=0):
            if user_number_check > 0:
                return
            if user_number_check % 10 == check_number:
                counter_check += 1
            user_number_check //= 10
            check_user_number(user_number_check, counter_check)

        check_user_number(user_number)
        count_number -= 1
        cnt += 1
        count_numbers(count_number, check_number, cnt, counter)

    count_numbers(count_number_user, check_number_user)


user_input()
