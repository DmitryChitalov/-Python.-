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

ii = 1100


def simple_numb_1(i):
    # O(n2) – квадратичная сложность
    lst = []
    n = i * 10
    for el in range(2, n + 1):
        for j in range(2, el):
            if el % j == 0:
                break
        else:
            lst.append(el)
    return lst[ii]


print(simple_numb_1(ii))


def simple_numb_2(i):
    # Логарифмическая сложность( но это не точно)
    series_of_numbers = []
    first_el = 2
    last_el = i * 10
    for el in range(last_el - 1):
        series_of_numbers.append(el + first_el)

    for el in series_of_numbers:
        if el * el < last_el:
            for further_el in series_of_numbers[el:]:
                if further_el % el == 0:
                    series_of_numbers.remove(further_el)
        else:
            break
    for idx, el in enumerate(series_of_numbers):
        if idx == i:
            return el


print(simple_numb_2(ii))

print(
    timeit.timeit(
        "simple_numb_1(ii)",
        setup="from __main__ import simple_numb_1, ii",
        number=10))

print(
    timeit.timeit(
        "simple_numb_2(ii)",
        setup="from __main__ import simple_numb_2, ii",
        number=10))
"""
Результат:
при i = 11
0.0012657559999999929
0.0007319999999999965

при i = 110
0.06895803900000001
0.04713836199999999

при i = 1100
6.180519304000001
4.581843181000001

Вывод: Решето Эратосфена дает ощутимый прирост скорости.
Вывод №2 первый алгоритм на столько плох, что не дает выигрыш даже при небольших числах.
"""
