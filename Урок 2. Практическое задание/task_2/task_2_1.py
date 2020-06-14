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

user_input = int(input('Введите натуральное число: '))
even_number = 0
odd_number = 0
while user_input:
    check_number = user_input % 10
    if check_number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    user_input //= 10

print(f'Введенное число содержит {even_number} четных и {odd_number} нечетных чисел')
