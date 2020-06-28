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


def check_number(user_number, count_even=0, count_odd=0):
    if user_number == 0:
        return count_odd, count_even
    else:
        numeral = user_number % 10
        user_number = user_number // 10
        if numeral % 2 == 0:
            count_even += 1
            return check_number(user_number, count_even, count_odd)
        else:
            count_odd += 1
            return check_number(user_number, count_even, count_odd)


print(f'Итого {check_number(112332)}')
