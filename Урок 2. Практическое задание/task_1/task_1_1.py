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
Введите первое число: 45
Введите второе число: 56
Результат 45 + 56 = 101
Введите операцию (+, -, *, / или 0 для выхода): rth
Неверная операция. Повторите ввод
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

OPERATION = input("Введите операцию (+, -, *, / или 0 для выхода): ")
while OPERATION != "0":
    if OPERATION == "+":
        NUMB_1 = float(input("Введите первое число: "))
        NUMB_2 = float(input("Введите второе число: "))
        print("Результат", str(NUMB_1), "+", str(NUMB_2), "=", str(NUMB_1 + NUMB_2))
    elif OPERATION == "-":
        NUMB_1 = float(input("Введите первое число: "))
        NUMB_2 = float(input("Введите второе число: "))
        print("Результат", str(NUMB_1), "-", str(NUMB_2), "=", str(NUMB_1 - NUMB_2))
    elif OPERATION == "*":
        NUMB_1 = float(input("Введите первое число: "))
        NUMB_2 = float(input("Введите второе число: "))
        print("Результат", str(NUMB_1), "*", str(NUMB_2), "=", str(NUMB_1 * NUMB_2))
    elif OPERATION == "/":
        NUMB_1 = float(input("Введите первое число: "))
        NUMB_2 = float(input("Введите второе число: "))
        if NUMB_2 == 0:
            print("На 0 делить нельзя, повторите ввод.")
        else:
            print("Результат", str(NUMB_1), "/", str(NUMB_2), "=", str(round(NUMB_1 / NUMB_2, 3)))
    else:
        print("Неверная операция. Повторите ввод")
    OPERATION = input("Введите операцию (+, -, *, / или 0 для выхода): ")
#    NUMB_1 = input("Введите первое число: ")
#    NUMB_2 = input("Введите второе число: ")
