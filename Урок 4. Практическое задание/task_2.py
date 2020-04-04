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
import math

primes_cached = [2, 3]


# Ищет указанное по порядку простое число
def find_prime_number(prime_position):
    # Задаем первые два числа
    primes = [2, 3]
    cur_pos = len(primes)
    cur_number = primes[cur_pos - 1] + 2
    while cur_pos < prime_position:
        is_prime = True
        for i in primes:
            # Не проверяем, если квадрат простого числа больше проверяемого
            if cur_number < i * i:
                break
            if cur_number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(cur_number)
            cur_pos += 1
        cur_number += 2
    return primes[prime_position - 1]


# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(10)", number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(100)", number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(1000)", number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(10000)", number=10) / 10)
# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(100000)", number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number", stmt="find_prime_number(1000000)", number=1))

# 4.070000000000011e-06
# 0.00011524099999999999
# 0.0035842619999999995
# 0.08927594999999999
# 2.2042147000000005
# 60.4520196
# Видно, как увеличение в десять раз, приводит к увеличению времени ~20-30 раз. Сложность примерно O(n log n)
# Проверяется не на каждое простое число, а только до корня из числа


# Ищет указанное по порядку простое число
def find_prime_number_cached(prime_position):
    # Задаем первые два числа
    global primes_cached
    cur_pos = len(primes_cached)
    cur_number = primes_cached[cur_pos - 1] + 2
    while cur_pos < prime_position:
        is_prime = True
        for i in primes_cached:
            # Не проверяем, если квадрат простого числа больше проверяемого
            if cur_number < i * i:
                break
            if cur_number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes_cached.append(cur_number)
            cur_pos += 1
        cur_number += 2
    return primes_cached[prime_position - 1]


# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(10)",
#                     number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(100)",
#                     number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(1000)",
#                     number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(10000)",
#                     number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(100000)",
#                     number=1))

# С использованием кэша. При однократном запуске
# 1.2699999999997436e-05
# 0.00020900000000000085
# 0.003995099999999998
# 0.0822777
# 2.2317794
# Как и в предыдущем случае, при росте аргумента в 10 раз, время выполнения растет в ~20-30 раз

# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(10)"))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(100)"))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(1000)"))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(10000)"))
# print(timeit.timeit(setup="from __main__ import find_prime_number_cached",
#                     stmt="find_prime_number_cached(100000)"))

# С использованием кэша. При множественном запуске
# 0.3632547
# 0.43131719999999996
# 0.47292959999999995
# 0.6153238000000001
# 3.3621152
# Время тратится на первый запуск. После этого результат берется из кэша за константу O(1)

BASE = 1000
GROWTH = 5


# Решето Эратосфена расширяется, пока не будет найден требуемый элемент
def find_prime_number_erath(prime_position):
    multiply = 1
    numbers = []
    res = []
    while len(res) < prime_position:
        left = BASE * (multiply // GROWTH)
        right = BASE * multiply
        numbers.extend(list(range(left, right)))
        numbers[1] = 0
        for i in numbers:
            if i:
                for j in range(i * 2, right, i):
                    numbers[j] = 0
        res = [i for i in numbers if i]
        multiply *= GROWTH
    return res[prime_position - 1]


# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(10)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(100)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(1000)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(10000)",
#                     number=10) / 10)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(100000)",
#                     number=1))
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath",
#                     stmt="find_prime_number_erath(1000000)",
#                     number=1))

# BASE = 500 и множитель 10
# 0.00012195600000000005
# 0.001085014
# 0.013486069
# 0.18117524000000002
# 2.2888811000000002
# 23.163811199999998
# При увеличении входного значения в 10 раз, время выполнения растет медленнее, в сравнении с первым алгоритмом
# Оценочная сложность алгоритма O(n log(log n)), взято из вики
# Время может отличаться из-за дополнительных расходов на выделение памяти
# Так при BASE = 1000 и множителе 5 будут результаты
# 0.00020310600000000002
# 0.00020269300000000005
# 0.007184070999999999
# 0.04023790000000001
# 1.5429137999999998
# 8.2953056
# Возможность строить решето постепенно позволяет избежать множества вычислений для малых чисел и позволяет более менее быстро построить решето для больших чисел


# Сложность лучше видно по решету, в который передается требуемый размер
def find_prime_number_erath_2(size):
    numbers = list(range(size))
    numbers[1] = 0
    for i in numbers:
        if i:
            for j in range(i * 2, size, i):
                numbers[j] = 0
    res = [i for i in numbers if i]
    return res


# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(100)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(1000)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(10000)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(100000)",
#                     number=100) / 100)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(1000000)",
#                     number=10) / 10)
# print(timeit.timeit(setup="from __main__ import find_prime_number_erath_2",
#                     stmt="find_prime_number_erath_2(10000000)",
#                     number=1))

# 2.7513000000000016e-05
# 0.000204229
# 0.002447647
# 0.026626682
# 0.38612271000000004
# 4.2862744
# В таком виде заметно, что сложность растет близко к линейной

# Как общий итог
# На небольших числах оба алгоритма работают достаточно быстро. С увеличением аргумента, сложность растет по-разному
# И в таком случае эффективнее оказывается решето Эратосфена
# Но, из-за того, что приходится хранить в памяти все числа, этот алгоритм будет требовательней к памяти