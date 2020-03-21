"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from re import sub


def reverse_number_function(
        initialize: bool = False,
        start: str = "1",
        number: int = 0,
        reverse_number: str = ""
) -> [dict, None]:
    if not initialize:
        start = sub(r"[\s]", "", input("Введите 1 для начала, или 0 для выхода из программы: "))

    if start == "0":
        return
    elif start == "1":
        if not initialize:
            try:
                print("Эта программа получает целое число и возвращает его в перевернутом виде")
                number = int(sub(r"[\s]", "", input("Введите целое число: ")))
            except ValueError:
                print("Вы ввели не целое число, попробуйте еще")
                return reverse_number_function(True, start)

        if number > 0:
            reverse_number += str(number % 10)
            number = number // 10
            reverse_number_function(True, start, number, reverse_number)
        else:
            print(int(reverse_number))
    else:
        print("Вы ввели неверное действие, попробуйте еще раз")
        reverse_number_function()


reverse_number_function()
