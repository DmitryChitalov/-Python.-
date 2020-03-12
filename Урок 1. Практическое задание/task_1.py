"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""


def sum_mult_digit() -> None:
    """ Сумма и произведение цифр 3-х значного числа """
    try:
        number = abs(int(
            input(
                "Пожалуста, введите целое 3-х значное число: ".strip())))
        if 100 <= number <= 999:
            number_first = number // 100
            number_second = (number // 10) % 10
            number_third = number % 10
            result_sum = number_first + number_second + number_third
            result_mult = number_first * number_second * number_third
            print(f"Для числа {number} сумма цифр равна {result_sum},"
                  f" произведение цифр равно {result_mult}")
        else:
            print(f"Введенное вами число {number} не корректно."
                  f" Число должно быть 3-х значное")
    except ValueError as err:
        print('Введенное Вами значение не является корректным числом')
        print('Ошибка: ', err)


if __name__ == "__main__":
    sum_mult_digit()
