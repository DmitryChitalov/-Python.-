"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion(number, result_number=0, oper_number=1):
    """
    Функция принимает на входе число
    Выводит на печать результат
    :return: завершение рекурсии, вывод результата
    """
    if number > 0:
        result_number += oper_number
        oper_number = oper_number / -2
        recursion(number - 1, result_number, oper_number)
    else:
        print(result_number)
        return


# запрашиваем ввод пользователя
USER_NUMBER = int(input('Введите число: '))
# вызываем нашу функцию recursion, передавая параметром число
recursion(USER_NUMBER)
