import timeit, math

def search_simple(n):
    if n == 1:
        return 2
    else:
        simple = 2
        simple_idx = 1
        div_count = 1
        num_for_check = 3
        while simple_idx < n:
            for i in range(2, int((num_for_check ** 0.5) + 1)):
                if num_for_check % i == 0:
                    div_count += 1
            if div_count == 1:
                simple = num_for_check
                simple_idx += 1
            num_for_check += 1
            div_count = 1
        return simple

def my_erat(n):
    sieve = [i for i in range(n * 10)]
    sieve[1] = 0
    j = 2
    while j < (n * 10):
        if sieve[j] != 0:
            for i in range(j * 2, n * 10, j):
                sieve[i] = 0
        j += 1
    return [num for num in sieve if num != 0][n - 1]


n = int(input("Введите номер простого числа: "))
print(f"Простое число №{n} по search_simple(n) равно {search_simple(n)}")
print(f"Простое число №{n} по my_erat(n) равно {my_erat(n)}")

print(timeit.timeit("search_simple(n)", setup = "from __main__ import search_simple, n", number = 100))
print(timeit.timeit("my_erat(n)", setup = "from __main__ import my_erat, n", number = 100))

"""
Результат
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
- мой простой - 0.004458699999999816
- моё решето - 0.005054200000000009

Время работы алгоритмов для поиска 100-го простого числа 100 раз:
- мой простой - 0.13641289999999984
- моё решето - 0.0627141

Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
- мой простой - 7.436533299999999
- моё решето - 0.9994730000000001

Алгоритм решета эффективен для поиска простых чисел с большим номером и чем больше номер, тем он выгоднее 
"""
