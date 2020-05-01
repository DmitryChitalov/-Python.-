"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def kalk():
    """
    Рекурсивная функция калькулятор
    """
    operation = input("Введите операцию (+, -, *, / или 0 для выхода: ")
    if operation == "0":
        return
    if operation in ('+', '-', '*', '/'):
        try:
            numb_1 = int(input("Введите первое число: "))
            numb_2 = int(input("Введите второе число: "))
            if operation == "+":
                print(f"Результат {numb_1 + numb_2}")
            elif operation == "-":
                print(f"Результат {numb_1 - numb_2}")
            elif operation == "*":
                print(f"Результат {numb_1 * numb_2}")
            elif operation == "/":
                while numb_2 == 0:
                    print(f"На ноль делить нельзя!!! Введите второе число ещё раз")
                    numb_2 = int(input("Введите второе число: "))
                print(f"Результат: {numb_1 / numb_2}")
        except ValueError:
            print("Вместо числа Вы ввели строку. Попробуйте ещё раз")
    else:
        print("Неверная операция, повторите ввод")
    kalk()


kalk()
