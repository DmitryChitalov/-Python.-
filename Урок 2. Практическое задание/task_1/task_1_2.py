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


# This is the most unpleasant thing that I wrote as part of training in GB.
# Recursion and human input are not compatible, like genius and villainy

def calc_recursion():
    """recursive operation input"""
    user_operation = input("Enter operation ( +, -, *, / ) or 0 to exit: ")
    if user_operation == '0':
        return
    if user_operation not in ('+', '-', '*', '/'):
        print("Unknown sign")
        calc_recursion()
    else:
        return calc_operation(user_operation)


def calc_operation(user_operation):
    """ Asks for operands and makes the calculations"""
    user_x = float(input("x = "))
    user_y = float(input("y = "))
    if user_operation == '+':
        print(f'{user_x} {user_operation} {user_y} = {(user_x + user_y):.2f}')
    elif user_operation == '-':
        print(f'{user_x} {user_operation} {user_y} = {(user_x - user_y):.2f}')
    elif user_operation == '*':
        print(f'{user_x} {user_operation} {user_y} = {(user_x * user_y):.2f}')
    elif user_y != 0:
        print(f'{user_x} {user_operation} {user_y} = {(user_x / user_y):.2f}')
    else:
        print("Zero division is not allowed")
        calc_recursion()
    return calc_recursion()


# Run
calc_recursion()
