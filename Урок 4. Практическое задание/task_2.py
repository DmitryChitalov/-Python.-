"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit


def simple_num(n):
    i = 1
    res = 2
    num = 3
    if n >= 1:
        while i != n:
            f = True
            for j in range(2, num):
                if num % j == 0:
                    f = False
                    break
            if f:
                res = num
                i += 1
            num += 1
        return res
    else:
        return 'Необходимо ввести целое число больше 0'


print('Алгоритм без решета')
print(
    timeit.timeit(
        'simple_num(10)',
        setup='from __main__ import simple_num',
        number=10))
print(
    timeit.timeit(
        'simple_num(100)',
        setup='from __main__ import simple_num',
        number=10))
print(
    timeit.timeit(
        'simple_num(1000)',
        setup='from __main__ import simple_num',
        number=1))


def simple_num_ert(n):
    c = n * 15
    a = [0] * c
    for i in range(c):
        a[i] = i
    a[1] = 0

    j = 2
    while j < c:
        if a[j] != 0:
            k = j * 2
            while k < c:
                a[k] = 0
                k += j
        j += 1
    b = []

    for el in a:
        if el != 0:
            b.append(el)
    return b[n - 1]


print('Алгоритм с использованием решета Эратосфена')
print(
    timeit.timeit(
        'simple_num_ert(10)',
        setup='from __main__ import simple_num_ert',
        number=10))
print(
    timeit.timeit(
        'simple_num_ert(100)',
        setup='from __main__ import simple_num_ert',
        number=10))
print(
    timeit.timeit(
        'simple_num_ert(1000)',
        setup='from __main__ import simple_num_ert',
        number=1))
print(
    timeit.timeit(
        'simple_num_ert(10000)',
        setup='from __main__ import simple_num_ert',
        number=1))
print(
    timeit.timeit(
        'simple_num_ert(100000)',
        setup='from __main__ import simple_num_ert',
        number=1))
# Аналитика.
# Без использования алгоритма решета Эратосфена перебор элементов происходил во вложенном цикле,
# сложность О(n**2), при увеличении индекса простого числа на порядок время выполнения увеличивается на два порядка.
# 0.00016473999999999656 10-е простое число
# 0.015226570000000002 100-е
# 0.282166198 1000-е
# За счет использования решета Эратосфена чем больший индекс числа мы ищем -
# тем больший выигрыш по производительности получаем, т.к. до этого были отфильтрованы большинство цифр.
# 0.0004436240000000313 10-е простое число
# 0.005525270999999998 100-е
# 0.006088760999999998 1000-е
# 0.06546991600000002 10 000-е
# 0.7664628750000001 100 000-е
