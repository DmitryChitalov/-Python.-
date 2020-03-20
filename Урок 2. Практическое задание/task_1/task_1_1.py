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


# Способ 1
def user_input():
    """
    Функция не принимает каких-либо значений
    :return: функция запрашивает ввод у пользователя двух чисел и возвращает их
    """
    user_number_a = int(input('Введите первое число: '))
    user_number_b = int(input('Введите второе число: '))
    return user_number_a, user_number_b


# дабы не путаться далее, введем переменные для кодов операций, а также для "0"
OP_PLUS = ord('+')
OP_MINUS = ord('-')
OP_MULT = ord('*')
OP_DIV = ord('/')
OP_ZERO = ord('0')

# бесконечный цикл, прервать который можно только введя на запрос операции "0"
while True:
    # будем использовать try-except, чтобы ловить моменты, когда введено больше одного символа
    try:
        # запрашиваем ввод знака операции
        USER_OPERATION = ord(input('Введите операцию (+, -, *, / или 0 для выхода): '))

        # проверяем соответствие знака, тем что мы хотим использовать
        # если "0", то цикл прерываем, если такого знака у нас нет, то ошибка
        if USER_OPERATION == OP_ZERO:
            break
        if USER_OPERATION == OP_PLUS:
            NUMBER_A, NUMBER_B = user_input()
            print(f'Результат {NUMBER_A} + {NUMBER_B} = {NUMBER_A + NUMBER_B}')
        elif USER_OPERATION == OP_MINUS:
            NUMBER_A, NUMBER_B = user_input()
            print(f'Результат {NUMBER_A} - {NUMBER_B} = {NUMBER_A - NUMBER_B}')
        elif USER_OPERATION == OP_MULT:
            NUMBER_A, NUMBER_B = user_input()
            print(f'Результат {NUMBER_A} * {NUMBER_B} = {NUMBER_A * NUMBER_B}')
        elif USER_OPERATION == OP_DIV:
            NUMBER_A, NUMBER_B = user_input()
            print(f'Результат {NUMBER_A} / {NUMBER_B} = {NUMBER_A / NUMBER_B}')
        else:
            print('Неверная операция. Повторите ввод')

    except TypeError:
        # если ловим строку, то выводим ошибку
        print('Неверная операция. Повторите ввод')
