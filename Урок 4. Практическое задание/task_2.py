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

import cProfile


# Генераторы

def test_any(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
           107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
           229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
           359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
           491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
           641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
           787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
           941, 947, 953, 967, 971, 977, 983, 991, 997]
    for i, item in enumerate(lst, start=1):
        assert func(i) == item, f'i = {i}, func(i)={func(i)}, lst[i] = {item}'
        print(f'Test {i} OK')


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


@memorize
def sieve(n):
    p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
              5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}
    for key in p_func.keys():
        if n <= key:
            length = p_func[key]
            break
    s = [x for x in range(2, length + 1) if
         x not in [i for sub in [list(range(2 * j, length + 1, j)) for j in range(2, length // 2)] for i in sub]]
    return s[n - 1]


test_any(sieve)

# timeit without memo
# task_2.sieve(10)"
# 1000 loops, best of 5: 2.92 msec per loop

# task_2.sieve(20)"
# 1000 loops, best of 5: 3.17 msec per loop

# timeit with memo

# task_2.sieve(10)"
# 1000 loops, best of 5: 170 nsec per loop

# task_2.sieve(20)"
# 1000 loops, best of 5: 180 nsec per loop

# task_2.sieve(100)"
# 1000 loops, best of 5: 161 nsec per loop

cProfile.run('sieve(10)')


# cProfile
# 105 function calls in 0.006 seconds - 10
# 1005 function calls in 0.365 seconds - 100

##################################################################################

# Dividers

@memorize
def prime(num):
    count = 1
    next_num = 2

    while count < num:
        next_num += 1
        for i in range(2, int(next_num ** 0.5) + 1):
            if next_num % i == 0:
                break
        else:
            count += 1
    return next_num


# test_any(prime)

# timeit without memo
# task_2.prime(10)"
# 1000 loops, best of 5: 15.2 usec per loop

# task_2.prime(20)"
# 1000 loops, best of 5: 39 usec per loop

# task_2.prime(50)"
# 1000 loops, best of 5: 144 usec per loop

# task_2.prime(100)"
# 1000 loops, best of 5: 373 usec per loop

# timeit with memo

# task_2.prime(10)"
# 1000 loops, best of 5: 181 nsec per loop

# task_2.prime(20)"
# 1000 loops, best of 5: 193 nsec per loop

# task_2.prime(50)"
# 1000 loops, best of 5: 168 nsec per loop

# task_2.prime(100)"
# 1000 loops, best of 5: 174 nsec per loop

cProfile.run('prime(1000)')


# cProfile
# 4 function calls in 0.000 seconds - 10
# 4 function calls in 0.001 seconds - 100
# 4 function calls in 0.013 seconds - 1000

##################################################################################

# Sieve

@memorize
def classic(n):
    p_func = {4: 10, 25: 10 ** 2, 168: 10 ** 3, 1229: 10 ** 4, 9592: 10 ** 5, 78498: 10 ** 6, 664579: 10 ** 7,
              5761455: 10 ** 8, 50847534: 10 ** 9, 455052511: 10 ** 10}
    for key in p_func.keys():
        if n <= key:
            length = p_func[key]
            break
    sieve = [0] * length
    for i in range(length):
        sieve[i] = i
    sieve[1] = 0
    m = 2

    while m < length:
        if sieve[m] != 0:
            j = m * 2
            while j < length:
                sieve[j] = 0
                j = j + m
        m += 1

    result = [x for x in sieve if sieve[x] != 0]
    return result[n - 1]


# test_any(classic)

# timeit without memo
# task_2.classic(10)"
# 1000 loops, best of 5: 27.2 usec per loop

# task_2.classic(100)"
# 1000 loops, best of 5: 323 usec per loop

# task_2.classic(1000)"
# 1000 loops, best of 5: 3.71 msec per loop

# timeit with memo

# task_2.classic(10)"
# 1000 loops, best of 5: 184 nsec per loop

# task_2.classic(100)"
# 1000 loops, best of 5: 174 nsec per loop

# task_2.classic(1000)"
# 1000 loops, best of 5: 297 nsec per loop

cProfile.run('classic(1000)')

# cProfile
# 6 function calls in 0.000 seconds - 10
# 6 function calls in 0.001 seconds - 100
# 6 function calls in 0.007 seconds - 1000

"""
Генераторы. Не удалось выполнить 1000 измерений 30-го числа, алгоритм слишком сложный из-за вложенных генераторов.
Кроме того, такой алгоритм крайне сложно отладить. Самое большое время на замерах без мемоизации. 
Сложность алгоритма O(n): внешний цикл проходит по каждому элементу исходного диапазона O(n), 
а для каждого элемента еще обрабатывается две строки сразу двух списков O(n^(1/2)) (проходов будет кол-во 
элементов^(1/2)). Итого O(n^(1/2)*n) = O(n^3/2).

Метод делителей выигрывает на небольших числах, но на втором месте для больших входных данных. Квадратичная сложность
O(n^2) из-за вложенных циклов с полным проходом.

Классический алгоритм решета Эратосфена выигрывает на больших числах с серьезным отрывом. Сложность алгоритма 
O(n log(log n)).

Мемоизация уравнивает все алгоритмы. При выборе алгоритма для решения конкретной задачи необходимо учитывать цели.
"""