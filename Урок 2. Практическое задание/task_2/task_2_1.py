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
num = 1
while num != 0:
    try:
        num = int(input('Введите натуральное число: '))
        if num == 0:
            print('Программа завершена!')
            break
        chet = 0
        nechet = 0
        while num != 0:
            if num // 10 != 0:
                if num % 10 % 2 != 0:
                    chet += 1
                else:
                    nechet += 1
                num = num // 10
                continue

            elif num // 10 == 0:
                if num % 2 != 0:
                    chet += 1
                else:
                    nechet += 1
                break
        print(
            f'В введенном числе всего {nechet + chet} цифр, из которых {nechet} чётных и {chet} нечётных')

    except Exception as e:
        print('Вы должны ввести натуральное число, или введите 0 для выхода!')
