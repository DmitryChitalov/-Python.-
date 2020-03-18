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


def num_enter(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


def result(num_1st, num_2nd, operation):
    if operation == '+':
        res = num_1st + num_2nd
    elif operation == '-':
        res = num_1st - num_2nd
    elif operation == '*':
        res = num_1st * num_2nd
    elif operation == '/':
        res = round(num_1st / num_2nd, 10)

    print(f"Result:\n"
          f"{num_1st} {operation} {num_2nd} = {res}")


while True:
    break_point = False
    while True:
        operation = input("Enter the operation (+, -, *, / or 0 to exit): ")
        if operation == '0':
            break_point = True
            break
        # elif operation not in ('+', '-', '*', '/'):
        elif operation != '+' and operation != '-' \
                and operation != '*' and operation != '/':
            print("Invalid operation. Repeat entry.")
        else:
            break
    if break_point:
        break

    num_1st = num_enter("Enter the first number: ")
    num_2nd = num_enter("Enter the second number: ")

    result(num_1st, num_2nd, operation)
