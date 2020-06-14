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

# First solution
# cont = True
# while cont:
#     try:
#         first_number = int(input("Enter first number: "))
#         second_number = int(input("Enter second number (it shouldn't be the zero!): "))
#         sign_operation = input("Enter the sigh for operation. '+', '-', '*', '/' or '0' to quit.:  ")
#
#         while True:
#             if sign_operation == '+':
#                 print(first_number + second_number)
#                 break
#             elif sign_operation == '-':
#                 print(first_number - second_number)
#                 break
#             elif sign_operation == '*':
#                 print(first_number * second_number)
#                 break
#             elif sign_operation == '/':
#                 print(first_number / second_number)
#                 break
#             elif sign_operation == '0':
#                 cont = False
#                 print('You entered a zero to quite. The calculation will be stopped')
#                 break
#             elif sign_operation not in ['0','+','-','*', '/']:
#                 print('You entered a wrong symbol. Try again')
#                 break
#     except ZeroDivisionError:
#         print("You are trying to divide by zero, it's wrong")

# Second solution

while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number (it shouldn't be the zero!): "))
    sign_operation = input("Enter the sigh for operation. '+', '-', '*', '/' or '0' to quit.:  ")

    if sign_operation == '0':
        print('You entered a zero to quite. The calculation will be stopped')
        break
    if sign_operation in {'+', '-', '*', '/'}:
        try:
            if sign_operation == '+':
                print(first_number + second_number)
            elif sign_operation == '-':
                print(first_number - second_number)
            elif sign_operation == '*':
                print(first_number * second_number)
            elif sign_operation == '/':
                print(first_number / second_number)
        except ZeroDivisionError:
            print("You are trying to divide by zero, it's wrong")
    else:
        print('Wrong sign for operation. Try again')
