"""
Задание 5.*
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
import timeit
n = int(input('Введите порядковый номер искомого простого числа: '))

def simple(i):
    """Без использования «Решета Эратосфена»"""
    result = []
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            result.append(n)
            if n >= i :
                break 
            count += 1
        n += 1
    return result



def sieve_eratosthenes(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0 
                j = j + m
        m += 1
    result = []
    for i in a:
        if a[i] != 0:
            result.append(a[i])
    return result        


# Мне пришлось модифицировать ваш алгоритм, что бы он выдавал массив, как и в алгоритме "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

print (f'n = {n}')
print(timeit.timeit("simple(n)", setup="from __main__ import simple, n", number=1000))
print(timeit.timeit("sieve_eratosthenes(n)", setup="from __main__ import sieve_eratosthenes, n", number=1000))
"""
n = 100
0.10930440000000097
0.024956300000001264

n = 1000
6.2776698
0.32272060000000025

n = 10000
498.0393276
3.393460300000015
"""
# Время растет нелинейно

