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
import cProfile
import math
# без решета


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
            else:
                count += 1

    return current_prime


print(timeit.timeit('prime(1000)', number=1, globals=globals()))
"""0.03879528"""
print(timeit.timeit('prime(10000)', number=1, globals=globals()))
"""0.21238105899999998"""
print(timeit.timeit('prime(100000)', number=1, globals=globals()))
"""1.7581763339999998"""
cProfile.run('prime (1000)')
"""4 function calls in 0.001 seconds"""
cProfile.run('prime (10000)')
"""4 function calls in 0.004 seconds"""
cProfile.run('prime (100000)')
"""4 function calls in 0.016 seconds"""
# время выполнения алгоритма значительно возрастает при поиске большего числа, что по всей видимости не очень эффективно

# c решетом Эратосфена, обнаружил данное решение, но почему-то оно менее эффектично нежели код "без решета"......


def prime_2(num):
    MULTIPLIER = 1.3
    size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30

    array = [True for _ in range(size)]
    array[:2] = [False, False]
    count = 0

    for i in range(2, size):
        if array[i]:
            count += 1
            if count == num:
                return i

            for j in range(i ** 2, size, i):
                array[j] = False


print(timeit.timeit('prime_2(1000)', number=1, globals=globals()))
print(timeit.timeit('prime_2(10000)', number=1, globals=globals()))
print(timeit.timeit('prime_2(100000)', number=1, globals=globals()))
# времмя выполнения алгоритма в зависимости от величины числа:
# 0.002176626000000015
# 0.028353755000000008
# 0.5149633499999999



