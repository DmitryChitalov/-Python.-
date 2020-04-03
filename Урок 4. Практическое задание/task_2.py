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
import timeit


def simple_nums(num):
    numbers = [i for i in range(2, num + 1)]
    lst = []
    for i in numbers:
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def eratosthenes(num):
    numbers = list(range(num + 1))
    numbers[1] = 0
    lst = []
    i = 2
    while i <= num:
        if numbers[i] != 0:
            lst.append(numbers[i])
            for j in range(i, num + 1, i):
                numbers[j] = 0
        i += 1
    return lst


def main():
    num = 1000
    simple_nums(num)
    eratosthenes(num)


cProfile.run('main()')
print(f"Выполение нахождения 10 по счету простого числа через подбор делителя: "
      f"{timeit.timeit('simple_nums(10)', setup='from __main__ import simple_nums', number=1000)} мс")
print(f"Выполение нахождения 10 по счету простого числа через Решето Эратосфена: "
      f"{timeit.timeit('eratosthenes(10)', setup='from __main__ import eratosthenes', number=1000)} мс")
print(f"Выполение нахождения 100 по счету простого числа через подбор делителя: "
      f"{timeit.timeit('simple_nums(100)', setup='from __main__ import simple_nums', number=1000)} мс")
print(f"Выполение нахождения 100 по счету простого числа через Решето Эратосфена: "
      f"{timeit.timeit('eratosthenes(100)', setup='from __main__ import eratosthenes', number=1000)} мс")
print(f"Выполение нахождения 1000 по счету простого числа через подбор делителя: "
      f"{timeit.timeit('simple_nums(1000)', setup='from __main__ import simple_nums', number=1000)} мс")
print(f"Выполение нахождения 1000 по счету простого числа через Решето Эратосфена: "
      f"{timeit.timeit('eratosthenes(1000)', setup='from __main__ import eratosthenes', number=1000)} мс")

"""
Решето Эратосфена имеет сложность алгоритма: O(n·log n)
Подбор делителя имеет квадратичную сложность (n2)
На основе замеров времени выполнения алгоритмов, на малых входных данных, скорость будет почти одинаковой,
но при увеличении значений эффективнее будет использовать Решето Эратосфена.
"""
