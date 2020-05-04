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

from timeit import Timer

# Вычисление n-го числа ряда Фибоначчи с помощью цикла while


def func_while():
    fib1 = fib2 = 1

    n = 10

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1


t1 = Timer("func_while()", "from __main__ import func_while")
print("func_while_test ", t1.timeit(number=10), "milliseconds")

# Рекурсивное вычисление n-го числа ряда Фибоначчи


def fibonacci(n=10):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


t2 = Timer("fibonacci()", "from __main__ import fibonacci")
print("fibonacci_test ", t2.timeit(number=10), "milliseconds")

# Вычисление n-го числа ряда Фибоначчи с помощью цикла for


def func_for():
    fib1 = fib2 = 1

    n = 10

    if n < 2:
        quit()

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2


t3 = Timer("func_for()", "from __main__ import func_for")
print("func_for_test ", t3.timeit(number=10), "milliseconds")


# Рекурсивный алгоритм является наиболее долгим, цикл while наиболле
# эффективный вариант для выполнения поставленной задачи
# func_while_test  3.5399999999990994e-05 milliseconds
# fibonacci_test  0.0005512000000000017 milliseconds
# func_for_test  4.020000000000412e-05 milliseconds
