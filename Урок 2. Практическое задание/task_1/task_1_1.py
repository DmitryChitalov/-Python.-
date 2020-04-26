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

import operator

# Чтобы не было цикла с ветвлениями if elif else
# создаем словарь с допустимыми операциями
DICT_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': lambda number_1, number_2: number_1 * number_2,
    '/': lambda number_1, number_2: number_1 / number_2
}


def calculation(operation, number_1, number_2):
    # Проверка запроса на запрещенную операцию  деления на 0
    if operation == '/' and number_2 == 0:
        print('Невозможно выполнить операцию! Операция деления на ноль является недопустимой!')
        return None
    else:
        return DICT_OPERATIONS[operation](number_1, number_2)


while True:
    # Запрос символа выполняемой операции
    OPERATION = input('Введите символ операции:\r\n'
                      'Для операции сложения чисел введите +,\r\n'
                      'Для вычисления разности чисел введите -,\r\n'
                      'Для выполнения умножения чисел введите *,\r\n'
                      'Для выполнения деления чисел введите / ,\r\n'
                      'Для завершения работы программы введите 0\r\n')
    # Проверка ввода символа завершения работы программы
    if OPERATION == '0':
        break
    # Проверка корректности введеного символа операции
    elif OPERATION in DICT_OPERATIONS.keys():
        while True:
            # Запрос ввода первого числа
            try:
                NUMBER_1 = float(input('Введите первое число: '))
            except (ValueError, TypeError):
                print('Ошибка ввода. Необходимо ввести число.')
            else:
                while True:
                    # Запрос ввода второго числа
                    try:
                        NUMBER_2 = float(input('Введите второе число: '))
                    except (ValueError, TypeError):
                        print('Ошибка ввода. Необходимо ввести число.')
                    else:
                        print(f'Результат выбранной операции {OPERATION}:\r\n'
                              f'{NUMBER_1} {OPERATION} {NUMBER_2} = {calculation(OPERATION, NUMBER_1, NUMBER_2)}')
                        break
                break
    else:
        print('Ошибка ввода операции! Введите символ операции из списка.')
