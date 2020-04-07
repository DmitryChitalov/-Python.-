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

"""
Урок 2
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import timeit


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number():
    while True:
        try:
            num = input(f"Введите положительное число\n")
            num = int(num)
            if num > 0:
                break
            else:
                print('Введено некорректное число')
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


def calc_formula(n):
    return n * (n + 1) // 2


def calc_cycle(n):
    res = 0
    for i in range(1, n + 1):
        res += i


# Первая часть вычисляет значение через формулу, сложность O(1)
# Вторая часть вычисляет через линейный цикл, сложность O(n)
print('calc_formula')
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(10)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(100)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(1000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(10000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(100000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_formula", stmt="calc_formula(1000000)", number=1000))

print('calc_cycle')
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(10)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(100)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(1000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(10000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(100000)", number=1000))
print(timeit.timeit(setup="from __main__ import calc_cycle", stmt="calc_cycle(1000000)", number=1000))

# Как видно из результата, по формуле высчитывается за одно и то же время
# В то время как через цикл, время увеличивается пропорционально увеличению аргумента
# calc_formula
# 0.00010600000000000193
# 0.00012859999999999955
# 0.00013979999999999895
# 0.00013979999999999895
# 0.00017780000000000226
# 0.0001708000000000022
# calc_cycle
# 0.0005381999999999991
# 0.0034561
# 0.04054939999999999
# 0.5269569
# 4.8001537