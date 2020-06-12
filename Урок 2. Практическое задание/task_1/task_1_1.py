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
inp = 1
lst = ['+', '-', '*', '/']
while inp != 0:
    inp = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if inp == '0':
        print('Программа завершена!')
        break
    elif inp not in lst:
        print('Введите корректную команду (+, -, *, / или 0 для выхода)')
        continue

    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except Exception as e:
        print('Вы должны ввести число!')
        continue

    if inp == '/' and num2 == 0:
        print('Деление на ноль невозможно!')
    elif inp == '+':
        print(f'Результат {num1} {inp} {num2} = {num1 + num2}')
    elif inp == '-':
        print(f'Результат {num1} {inp} {num2} = {num1 - num2}')
    elif inp == "*":
        print(f'Результат {num1} {inp} {num2} = {num1 * num2}')
    elif inp == '/':
        print(f'Результат {num1} {inp} {num2} = {num1 / num2}')
