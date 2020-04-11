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


def sorting_divisor(i_simple_num):
    """
    Функция - перебор делителей для поиска i'того простого числа.

    :param i_simple_num: номер искомого простого числа
    :return:
    """
    sieve = [2]
    first_num = 3
    while len(sieve) < i_simple_num:
        for itm in sieve:
            if first_num % itm != 0:
                if itm == sieve[-1]:
                    sieve.append(first_num)
                    first_num += 1
                    break
            else:
                first_num += 1
                break
    return sieve[i_simple_num-1]


def eratosfen(i_simple_num):
    """
    Функция - решето Эратосфена, получает номер простого числа,
    которое необходимо найти и "просеивает" целых чисел, пока
    в нем не останутся только простые числа, затем по индексу
    возвращает нужное число.

    :param i_simple_num: номер искомого простого числа
    :return:
    """
    if i_simple_num <= 10:
        simple_num = 30
    elif i_simple_num <= 100:
        simple_num = 542
    elif i_simple_num <= 1000:
        simple_num = 7920
    elif i_simple_num <= 5000:
        simple_num = 48612
    elif i_simple_num <= 10000:
        simple_num = 104730
    else:
        simple_num = sorting_divisor(i_simple_num) + 1

    num_list = [num for num in range(simple_num)][2:]
    for num in num_list:
        if num:
            num_list[num*num - 2::num] = [0] * len(num_list[num*num - 2::num])
    num_list = sorted(set(num_list))[1:]
    return num_list[i_simple_num - 1]


def main():
    print('Алгоритм без решета. 10: ',
          timeit.timeit(
              'sorting_divisor(10)',
              setup='from __main__ import sorting_divisor',
              number=100))
    print('Решето Эратосфена. 10: ',
          timeit.timeit(
              'eratosfen(10)',
              setup='from __main__ import eratosfen',
              number=100))

    print('Алгоритм без решета. 100: ',
          timeit.timeit(
              'sorting_divisor(100)',
              setup='from __main__ import sorting_divisor',
              number=100))
    print('Решето Эратосфена. 100: ',
          timeit.timeit(
              'eratosfen(100)',
              setup='from __main__ import eratosfen',
              number=100))

    print('Алгоритм без решета. 1000: ',
          timeit.timeit(
              'sorting_divisor(1000)',
              setup='from __main__ import sorting_divisor',
              number=100))
    print('Решето Эратосфена. 1000: ',
          timeit.timeit(
              'eratosfen(1000)',
              setup='from __main__ import eratosfen',
              number=100))
    print('Решето Эратосфена. 10000: ',
          timeit.timeit(
              'eratosfen(10000)',
              setup='from __main__ import eratosfen',
              number=100))

# main()

"""
Алгоритм без решета. 10:  0.0021405999999999925
Решето Эратосфена. 10:  0.001507200000000014
Алгоритм без решета. 100:  0.1131586
Решето Эратосфена. 100:  0.018082199999999965
Алгоритм без решета. 1000:  12.8595606
Решето Эратосфена. 1000:  0.1934312000000009
Решето Эратосфена. 10000:  4.675514600000001

Решето Эратосфена - уже при нахождении 10 первых простых чисел, совсем немного, 
но стабильно превосходит обычный алгоритм на циклах, но при нахождении 100 или 
тем более 1000 простых чисел, превосходство алгоритма решета становится очевидным 
(в 5 и 40 раз соответственно).
Это связано со сложностью алгоритмов, которую для каждой функции можно оценить как:
O(n**2) - алгоритм без решета
O(n log n) - решето Эратосфена
"""

# Пропустим обе функции через cProfile

print(cProfile.run('sorting_divisor(1000)'))
print(cProfile.run('eratosfen(1000)'))

"""
Результат работы cProfile:
         8921 function calls in 0.103 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.103    0.103 <string>:1(<module>)
        1    0.101    0.101    0.103    0.103 task_2.py:19(sorting_divisor)
        1    0.000    0.000    0.103    0.103 {built-in method builtins.exec}
     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
         1006 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.002    0.002    0.003    0.003 task_2.py:35(eratosfen)
        1    0.001    0.001    0.001    0.001 task_2.py:49(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
cProfile - как я понял не совсем корректно отобразил количество итераций 
в цикле - как вызовы len, но чисто логически мы понимаем, что именно 7918
итераций необходим для нахождения тысячного простого числа, с использованием
алгоритма без решета, кроме того алгоритм без решета 999 раз вызывает метод
append, что так-же сказывается на производительности.
В свою очередь решето лишено этих недостатков, ему необходимо 1000 раз
"просеять" массив, чтоб получить желаемый результат. Я вижу в решете
только один, но значительный недостаток, нам нужно заранее знать,
сколько чисел добавить в исходный массив, который будем сеять.
Возможно алгоритм сегментированного решета решает эту проблему, но
реализовать его в коде у меня не получилось. В итоге, если бы мне понадобилось
найти, например 15648 простое число, мне пришлось бы использовать алгоритм
без решета - перебор делителей, до нужного простого числа.
Можно, конечно, установить заведомо подходящее число элемментов, например n**2
скорее всего удовлетворит всем простым числам, но эффективность такого подхода
вызывает у меня некоторые сомнения.
"""
