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

def calc():
    """
    Функция calc() производит арифметические вычисления для пользователя.

    Функция вызывается рекурсивно до тех пор, пока пользователь не введёт '0'.
    """
    # Запрос ввода типа операции
    oper = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    # Валидация входных значений
    if oper not in ('+', '-', '*', '/', '0'):
        print('Неизвестная опреация. Повторите ввод.')
        return calc()
    if oper == '0':
        print('До свидания!')
        return 'Работа программы завершена.'
    try:
        # Запрос на ввод первого и второго числа
        # (слагаемые, уменьшаемое/вычитаемое, множители, делимое/делитель)
        # Обрабатываются исключения связанные со вводом не цифр
        first_num = float(input('Введите первое число: '))
        second_num = float(input('Введите второе число: '))
        # Явно объявить переменную просил PyCharm, т.к. до стр.72 могло не дойти ни одного значения
        result = 0
        # В зависимости от выбранного типа операции, происходит вычисление
        if oper == '+':
            result = first_num + second_num
        elif oper == '-':
            result = first_num - second_num
        elif oper == '*':
            result = first_num * second_num
        elif oper == '/':
            if second_num == 0:
                print('На ноль делить нельзя! Введите другие числа.')
                # делитель не может ровняться 0, функция вызывается повторно
                return calc()
            result = first_num / second_num
        # Результат вычислений выводится в консоль и функция рекурсивно вызывает сама себя
        print(f'Результат вычислений: {result}')
        return calc()
    except ValueError:
        print('Необходимо вводить цифры!')

CALCULATE = calc()
