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

# ввод числа
user_number = input('введите число')

# обработка
i = cuantity = len(user_number)
number = int(user_number)
even = 0
odd = 0

while i != 0:
    # print(number)
    test = number % 2
    if test == 0:
        even = even +1
    else:
        odd = odd +1
    number = number // 10
    i = i - 1

# вывод
print(f'В числе {user_number} всего {cuantity} цифр, из которых {even} чётных и {odd} нечётных' )

