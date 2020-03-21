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
try:
    NUMBERS = int(input('Введите число : '))
    if NUMBERS > 0:
        EVEN_SCORE = 0
        NOT_EVEN_SCORE = 0
        COUNT_OF_NUMBERS = 0
        for el in str(NUMBERS):
            COUNT_OF_NUMBERS += 1
            if int(el) % 2 == 0:
                EVEN_SCORE += 1
            else:
                NOT_EVEN_SCORE += 1
        print(f'В числе {NUMBERS} всего {COUNT_OF_NUMBERS} цифр ,'
              f'из которых четных цифр : {EVEN_SCORE} и нечетных цифр : {NOT_EVEN_SCORE}')
    else:
        raise IOError
except ValueError:
    print('Некорректное значение.Введите натуральное число.')
except IOError:
    print('Натуральное числа начинаются с 1 ')

