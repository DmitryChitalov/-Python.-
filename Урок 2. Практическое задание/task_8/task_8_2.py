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


def recursion(source_number, count_number, result_number=0, iterator=1):
    """
    Функция принимает в виде значения искокомое число и количество вводимых чисел
    Параметр результата по умолчанию задан 0, итератор 1
    :return: завершение рекурсии, вывод результата
    """
    if count_number == 0:
        print(f'Было введено {result_number} цифр "{source_number}"')
        return
    else:
        user_number = int(input(f'Число {iterator}: '))
        while user_number > 0:
            # проверяем равна ли цифра искомой, если да, то увеличиваем счетчик
            if user_number % 10 == source_number:
                result_number += 1
            user_number = user_number // 10
        count_number -= 1
        iterator += 1
        recursion(source_number, count_number, result_number, iterator)


# запрашиваем ввод пользователя
COUNT_NUMBER = int(input('Сколько будет чисел? '))
SOURCE_NUMBER = int(input('Какую цифру считать? '))

# вызываем нашу функцию recursion
recursion(SOURCE_NUMBER, COUNT_NUMBER)
