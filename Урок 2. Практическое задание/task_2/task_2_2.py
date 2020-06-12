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
chet = 0
nechet = 0


def recurs():
    try:
        num = int(input('Введите натуральное число: '))
    except Exception as e:
        print('Вы должны ввести натуральное число, или введите 0 для выхода!')
        return recurs()

    else:
        def recurs1(num):
            global chet
            global nechet
            if num // 10 != 0:
                if num % 10 % 2 != 0:
                    chet += 1
                else:
                    nechet += 1
                return recurs1(num // 10)

            elif num // 10 == 0:
                if num % 2 != 0:
                    chet += 1
                else:
                    nechet += 1
            print(
                f'В введенном числе всего {nechet + chet} цифр, из которых {nechet} чётных и {chet} нечётных')

        recurs1(num)


recurs()
