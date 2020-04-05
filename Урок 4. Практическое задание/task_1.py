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
import dis
"""первый пример"""


A_NUMB = 123
A_1_NUMB = A_NUMB // 100
A_2_NUMB = (A_NUMB // 10) % 10
A_3_NUMB = A_NUMB % 10

B_NUMB = A_1_NUMB + A_2_NUMB + A_3_NUMB
C_NUMB = A_1_NUMB * A_2_NUMB * A_3_NUMB

print(f"Сумма цифр трехзначного числа: {B_NUMB}")
print(f"Произведение цифр трехзначного числа: {C_NUMB}")

"""второй пример"""
def fun(number, a=0, b=0):
    if number == 0:
        return a, b
    else:
        c= number % 10
        number = number // 10
        if c % 2 == 0:
            a += 1
            return fun(number, a, b)
        else:
            b += 1
            return fun(number, a, b)

NUMBER = 14
print(f"{fun(NUMBER)}")

print(timeit.timeit("""
A_NUMB = 123
A_1_NUMB = A_NUMB // 100
A_2_NUMB = (A_NUMB // 10) % 10
A_3_NUMB = A_NUMB % 10

B_NUMB = A_1_NUMB + A_2_NUMB + A_3_NUMB
C_NUMB = A_1_NUMB * A_2_NUMB * A_3_NUMB
"""))

"""time = 0.1980031000000002"""

print(
    timeit.timeit(
        "fun(NUMBER)",
        setup="from __main__ import fun, NUMBER",
        number=1000))
"""time = 0.0007620999999997657"""
"""Второй пример быстрее, так как здесь отрабатывает функция"""

"""Оптимизация"""
def fun_1(a):
    a_1_numb = a // 100
    a_2_numb = (a // 10) % 10
    a_3_numb = a % 10
    b_numb = a_1_numb + a_2_numb + a_3_numb
    c_numb = a_1_numb * a_2_numb * a_3_numb
    return b_numb, c_numb

A = 123
print(f"{fun_1(A)}")
print(
    timeit.timeit(
        "fun_1(A)",
        setup="from __main__ import fun_1, A",
        number=1000))
"""time = 0.0002920999999999896 - функция отработала быстрее, как и в первом пункте."""

"""для второго случая логичнее всего сделать через декоратор, тогда на обработку потребуется меньше времени"""
def memorize(fun_rec):
    print(memory)
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = fun_rec(n)
            memory[n] = r
        return r
    return g

@memorize
def fun_rec(number, a=0, b=0):
     if number == 0:
         return a, b
     else:
        c = number % 10
        number = number // 10
        if c % 2 == 0:
            a += 1
            return fun_rec(number, a, b)
        else:
            b += 1
            return fun_rec(number, a, b)

print(dis.dis(fun_rec))
NUMBER = 14
print(timeit.timeit("fun_rec(NUMBER)", setup="from __main__ import NUMBER"))
