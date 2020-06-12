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


def odd_even_recurs(user_input, even_number=0, odd_number=0):
    if user_input == 0:
        return print(f'Введенное число содержит {even_number} четных и {odd_number} нечетных чисел')
    else:
        check_number = user_input % 10
        if check_number % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    user_input //= 10
    return odd_even_recurs(user_input, even_number, odd_number)


odd_even_recurs(int(input('Введите натуральное число: ')))
