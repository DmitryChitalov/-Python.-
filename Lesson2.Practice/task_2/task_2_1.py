"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def digit_counter(num):
    """
    Реализация через цикл
    """

    odd = 0
    even = 0
    users_num = num
    while num > 0:
        result = num % 10
        if result % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
        print(num)
    return f'В числе {users_num} всего {odd + even} цифры, ' \
           f'из которых {even} чётных и {odd} нечётных'


print(digit_counter(17871924))
