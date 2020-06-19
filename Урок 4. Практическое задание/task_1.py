"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit

"""
Пример сравнения 1
"""


# First solution


def first_function():
    cont = True
    while cont:
        first_number = 123456789
        second_number = 123456789
        sign_operation = '*'

        if sign_operation == '+':
            return first_number + second_number
        elif sign_operation == '-':
            return first_number - second_number
        elif sign_operation == '*':
            return first_number * second_number
        elif sign_operation == '/':
            return first_number / second_number
        elif sign_operation == '0':
            return 'You entered a zero to quite. The calculation will be stopped'

        elif sign_operation not in ['0', '+', '-', '*', '/']:
            return 'You entered a wrong symbol. Try again'


# first_function()
print(timeit.timeit("first_function()", setup="from __main__ import first_function", number=1000))


# Second solution


def second_function():
    first_number = 123456789
    second_number = 123456789
    sign_operation = '*'

    if sign_operation == '0':
        print('You entered a zero to quite. The calculation will be stopped')
    if sign_operation in {'+', '-', '*', '/'}:
        try:
            if sign_operation == '+':
                return first_number + second_number
            elif sign_operation == '-':
                return first_number - second_number
            elif sign_operation == '*':
                return first_number * second_number
            elif sign_operation == '/':
                return first_number / second_number
        except ZeroDivisionError:
            return "You are trying to divide by zero, it's wrong"
    else:
        return 'Wrong sign for operation. Try again'


# second_function()
print(timeit.timeit("second_function()", setup="from __main__ import second_function", number=1000))


# Third solution


def third_function():
    OPER_TYPE = '*'
    if OPER_TYPE in "+-*/":
        try:
            NUM_1 = 123456789
            NUM_2 = 123456789
            if OPER_TYPE == '+':
                RES = NUM_1 + NUM_2
            if OPER_TYPE == '-':
                RES = NUM_1 - NUM_2
            if OPER_TYPE == '*':
                RES = NUM_1 * NUM_2
            if OPER_TYPE == '/':
                if NUM_2 != 0:
                    RES = NUM_1 / NUM_2
                else:
                    print("Error. Divide by zero! Try again")
            return f"Result {NUM_1} {OPER_TYPE} {NUM_2} = {RES}"
        except ValueError:
            return "You entered a wrong value. Please correct it."
    else:
        return "Wrong operation. Try repeat again"


# third_function()
print(timeit.timeit("third_function()", setup="from __main__ import third_function", number=1000))

"""
Первые две фунцкии отрабатывают одинаково быстро, поскольку реализация в целом похожая на замерах 1000 запусков
0.0002571719999999722
0.00023741999999993268
0.0007426790000000238
Но третья функция медленнее почти всегда на 0,005 секунды

"""
# =======================================================================================================================
"""
Пример сравнения 2 - Во втором массиве сохранить индексы четных элементов первого массива
"""
import random


#  Solution with cycle


def generator_function():
    initial = [random.randint(1, 100) for item in range(1000)]
    final = []
    for num in initial:
        if num % 2 == 0:
            final.append(initial.index(num))
        else:
            continue
    return final


print(timeit.timeit("generator_function()", setup="from __main__ import generator_function", number=1000))


# Solution with cycle
def cycle_function():
    initial = [random.randint(1, 100) for item in range(1000)]
    return [num for num in range(len(initial) + 1) if num % 2 == 0]


print(timeit.timeit("cycle_function()", setup="from __main__ import cycle_function", number=1000))

"""
Первая функция через цикл for на замерах 1000 запусков работает в 2 раза медленее чем вторая реализованная через
генератор. Разница почти в 2 раза
2.126314305
1.251248333
"""

# =======================================================================================================================
"""
Пример сравнения 3 - В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 

"""


# solution with fucntion and cycle for


def func_cycle_range():
    final = []
    for x in range(2, 10):
        multiples = 0
        for y in range(2, 100):
            if y % x == 0:
                multiples += 1
        final.append(f"В диапазоне 2-99: {multiples} чисел кратны {x}")
    return '\n'.join(final)


print(timeit.timeit("func_cycle_range()", setup="from __main__ import func_cycle_range", number=1000))


def func_gen_range():
    final = []
    for i in range(2, 10):
        new_list = [el for el in range(2, 100) if el % i == 0]
        final.append(f"В диапазоне 2-99: {len(new_list)} чисел кратны {i}")
    return '\n'.join(final)


print(timeit.timeit("func_gen_range()", setup="from __main__ import func_gen_range", number=1000))

"""
Странно, но функция func_cycle_range() с двумя вложенными циклами быстрее чем 
функция func_gen_range() с 1 вложенным циклом и генератором. 
Почему?

0.05109987599999943
0.052662662999999554
"""
