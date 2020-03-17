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


def recursion_counter() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ """

    def recursion(r_value, r_count, r_evens, r_odds) -> tuple:
        if r_value <= 0:
            return r_count, r_evens, r_odds

        r_count += 1
        number = r_value % 10
        if number % 2 == 0:
            r_evens += 1
        else:
            r_odds += 1
        r_value = r_value // 10
        r_count, r_evens, r_odds = recursion(r_value, r_count, r_evens, r_odds)
        return r_count, r_evens, r_odds

    try:
        value = int(input('Введите число: ').strip())
        user_input = value

        if value <= 0:
            print('Недопустимое значение. Выходим')
        else:
            count, evens, odds = recursion(value, 0, 0, 0)
            print(
                f'В числе {user_input} всего {count} цифр, '
                f'из которых {evens} чётных и {odds} нечётных'
            )
    except ValueError:
        print('Недопустимое значение. Выходим')


if __name__ == "__main__":
    recursion_counter()
