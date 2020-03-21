"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from re import sub


def sum_consequence(
        initialize: bool = False,
        start: str = "1",
        number_of_steps: int = 0,
        number: int = 1,
        even: bool = True
) -> [float, None]:
    if not initialize:
        start = sub(r"[\s]", "", input("Введите 1 для начала, или 0 для выхода из программы: "))

    if start == "0":
        return
    elif start == "1":
        if not initialize:
            try:
                print("Эта программа выводит сумму последовательности чисел 1 -0.5 0.25 -0.125 ... из N элементов")
                number_of_steps = int(
                    sub(r"[\s]", "", input("Введите сколько числе последовательности нужно сложить: "))
                ) - 1
            except ValueError:
                print("Вы ввели не целое число, попробуйте еще")
                return sum_consequence(True, start)

        if number_of_steps > 0:
            number += number * (-0.5) if even else number * 0.5
            number_of_steps -= 1

            return sum_consequence(True, start, number_of_steps, number, not even)
        else:
            return number
    else:
        print("Вы ввели неверное действие, попробуйте еще раз")
        return sum_consequence()


print(sum_consequence())
