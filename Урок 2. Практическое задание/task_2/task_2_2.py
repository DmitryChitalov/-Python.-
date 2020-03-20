"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursion(number, even_number=0, odd_number=0):
    """
    Функция принимает на входе число и счетчики
    По-умолчанию счетчики равны нулю
    :return: завершение рекурсии, вывод результата
    """
    if number == 0:
        print(f'Количество четных и нечетных цифр в числе равно: ({even_number}, {odd_number})')
        return

    if number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    number = number // 10
    recursion(number, even_number, odd_number)


# запрашиваем ввод пользователя
USER_NUMBER = int(input('Введите натуральное число: '))

# вызываем нашу функцию recursion, передавая параметром число
recursion(USER_NUMBER)
