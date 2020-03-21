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

from re import sub


def count_even_odd_digits(start: str = "1", number: int = 0, count: int = 0, even: int = 0, odd: int = 0) -> [dict, None]:
    if count == 0:
        start = sub(r"[\s]", "", input("Введите 1 для начала, или 0 для выхода из программы: "))

    if start == "0":
        return
    elif start == "1":
        if count == 0:
            try:
                print("Это программа которая считает четные и нечетные цифры в натуральном числе")
                number = int(sub(r"[\s]", "", input("Введите целое число: ")))
            except ValueError:
                print("Вы ввели не целое число, попробуйте еще")
                return count_even_odd_digits(start)

        if number > 0:
            if number % 10 % 2 == 0:
                even += 1
            else:
                odd += 1

            count += 1
            next_value = number // 10
            count_even_odd_digits(start, next_value, count, even, odd)
        else:
            print({"even": even, "odd": odd})
    else:
        print("Вы ввели неверное действие, попробуйте еще раз")
        count_even_odd_digits()


count_even_odd_digits()
