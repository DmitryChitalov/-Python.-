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


def operands():
    x = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if x == '+' or x == '-' or x == '*' or x == '/':
        return x
    elif x == '0':
        return 'exit'
    else:
        return 'Неверная операция. Повторите ввод'


def get_digits():
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    return first, second


def operations(operand, first, second):
    if operand == 0:
        return 'exit'
    elif operand == '+':
        return f'Результат {first} {operand} {second} = {first + second}'
    elif operand == '-':
        return f'Результат {first} {operand} {second} = {first - second}'
    elif operand == '*':
        return f'Результат {first} {operand} {second} = {first * second}'
    elif operand == '/':
        return f'Результат {first} {operand} {second} = {first / second}'
    else:
        return 'Неверная операция. Повторите ввод'


while True:
    operand = operands()
    if operand == 'exit':
        break
    result = operations(operand, *get_digits())
    if result == 'exit':
        break
    elif result == 'Неверная операция. Повторите ввод':
        print(result)
        continue
    else:
        print(result)
