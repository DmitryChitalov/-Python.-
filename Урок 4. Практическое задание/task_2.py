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


# Без использования «Решета Эратосфена»
def prime_nums():
    list_nums = []
    for num in range(2, n + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            list_nums.append(num)
    return list_nums


# Используя алгоритм «Решето Эратосфена»
def eratosthen():
    multiples = []
    results = []
    for i in range(2, n + 1):
        if i not in multiples:
            results.append(i)
            for j in range(i * i, n + 1, i):
                multiples.append(j)

    return results


n = 1000
print(prime_nums())
print(eratosthen())

number = 100
t1 = timeit.Timer("prime_nums()", setup="from __main__ import prime_nums")
print("prime_nums() - ", t1.timeit(number=number), "milliseconds")
t2 = timeit.Timer("eratosthen()", setup="from __main__ import eratosthen")
print("eratosthen() - ", t1.timeit(number=number), "milliseconds")


"""
Исходя из результатов оба алгоритма выполняюьтся примерно одинаково по времени. Я считаю, что эта разница
не значительная и ей можно пренебречь:
prime_nums() -  6.9896962 milliseconds
eratosthen() -  6.7909139 milliseconds

Оценка сложности алгоритмов:
1. prime_nums()
Здесь с оценкой у меня возникли сложности.
У нас есть один внешний цикл - его сложность О(n).
Внутри у него есть еще один цикл - у него сложность меняется от О(1) до О(n).
Соотвественно средняя сложность цикла - О(n/2).
В итоге обща сложность алгоритма - О(n*(n/2)) -> О(n^2)

2. eratosthen()
Мы проходим по двум циклам с максимальным количеством итераций n. Один цикл находится внутри другого.
Следовательно сложность данного алгоритма О(n^2)
"""