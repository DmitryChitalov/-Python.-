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

N1 = 10
N2 = 100
N3 = 1000

def search_1(N):     # Метод перебора
    NUMBERS = []
    for i in range(2, N + 1):
        for j in NUMBERS:
            if i % j == 0:
                break
        else:
            NUMBERS.append(i)
    return NUMBERS

print(timeit.timeit(f"search_1({N1})", setup="from __main__ import search_1", number=1000))
print(timeit.timeit(f"search_1({N2})", setup="from __main__ import search_1", number=1000))
print(timeit.timeit(f"search_1({N3})", setup="from __main__ import search_1", number=1000))

def search_2(N):          # Решето Эратосфена
    a = [x for x in range(N+1)]
    a[1] = 0
    NUMBERS = []
    i = 2
    while i <= N:
        if a[i] != 0:
            NUMBERS.append(a[i])
            for j in range(i, N + 1, i):
                a[j] = 0
        i += 1
    return NUMBERS

print(timeit.timeit(f"search_2({N1})", setup="from __main__ import search_2", number=1000))
print(timeit.timeit(f"search_2({N2})", setup="from __main__ import search_2", number=1000))
print(timeit.timeit(f"search_2({N3})", setup="from __main__ import search_2", number=1000))

# Метод перебора:
# n = 10 :   0.002659799999999997
# n = 100 :  0.05638989999999999
# n = 1000 : 1.5560931

# Решето Эратосфена
# n = 10 :   0.005019399999999896
# n = 100 :  0.03706179999999981
# n = 1000 : 0.4329491000000001

# При n = 10 выполнение Методом перебора производится быстрее,
# но уже при n = 100 использование Решета Эратосфена становится эффективней,
# при n = 1000 - выигрыш по времени у второго варианта очвиден.
# Сложность первого алгоритма - O(n**2), второго - O(n log(log n))
