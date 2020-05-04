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


def eratosfen_method(max_number):
    a = [i for i in range(max_number * 10)]
    a[1] = 0
    i = 2
    while i < max_number * 10:
        if a[i] != 0:
            j = i * 2
            while j < max_number * 10:
                a[j] = 0
                j += i
        i += 1

    number = []
    for value in a:
        if len(number) < max_number:
            if value != 0:
                number.append(value)
    return number, f'{max_number} по счету простое число: {number[-1]}'


def find_simple_numbers(max_number):
    n = max_number
    lst = []
    first = 2
    while len(lst) != max_number:
        for i in range(first, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        n += 1
        first = n
    return lst, f'{max_number} по счету простое число: {lst[-1]}'


# Замер времени при поиске 10-го простого числа
MAX_NUMBER = 10
print(f'\nПоиск 10-го простого числа')
print(f'Результат по алгоритму "Решето Эратосфена":\n{eratosfen_method(MAX_NUMBER)[1]}')
print(f'Результат другого метода:\n{find_simple_numbers(MAX_NUMBER)[1]}')

time_eratosfen_method = timeit.timeit("eratosfen_method(MAX_NUMBER)",
                                      setup="from __main__ import eratosfen_method, MAX_NUMBER",
                                      number=1000)

time_find_simple_numbers = timeit.timeit("find_simple_numbers(MAX_NUMBER)",
                                         setup="from __main__ import find_simple_numbers, MAX_NUMBER",
                                         number=1000)

print(f'\nЗатраченное время на исполнение'
      f'\n{"- Используя алгоритм «Решето Эратосфена»:":25} {time_eratosfen_method}'
      f'\n{"- Без использования «Решета Эратосфена»:":25} {time_find_simple_numbers}')

# Замер времени при поиске 100-го простого числа
MAX_NUMBER = 100
print(f'\nПоиск 100-го простого числа')
print(f'Результат по алгоритму "Решето Эратосфена":\n{eratosfen_method(MAX_NUMBER)[1]}')
print(f'Результат другого метода:\n{find_simple_numbers(MAX_NUMBER)[1]}')

time_eratosfen_method = timeit.timeit("eratosfen_method(MAX_NUMBER)",
                                      setup="from __main__ import eratosfen_method, MAX_NUMBER",
                                      number=1000)

time_find_simple_numbers = timeit.timeit("find_simple_numbers(MAX_NUMBER)",
                                         setup="from __main__ import find_simple_numbers, MAX_NUMBER",
                                         number=1000)

print(f'\nЗатраченное время на исполнение '
      f'\n{"- Используя алгоритм «Решето Эратосфена»:":25} {time_eratosfen_method}'
      f'\n{"- Без использования «Решета Эратосфена»:":25} {time_find_simple_numbers}')

# Замер времени при поиске 1000-го простого числа
MAX_NUMBER = 1000
print(f'\nПоиск 1000-го простого числа')
print(f'Результат по алгоритму "Решето Эратосфена":\n{eratosfen_method(MAX_NUMBER)[1]}')
print(f'Результат другого метода:\n{find_simple_numbers(MAX_NUMBER)[1]}')

time_eratosfen_method = timeit.timeit("eratosfen_method(MAX_NUMBER)",
                                      setup="from __main__ import eratosfen_method, MAX_NUMBER",
                                      number=10)

time_find_simple_numbers = timeit.timeit("find_simple_numbers(MAX_NUMBER)",
                                         setup="from __main__ import find_simple_numbers, MAX_NUMBER",
                                         number=10)

print(f'\nЗатраченное время на исполнение '
      f'\n{"- Используя алгоритм «Решето Эратосфена»:":25} {time_eratosfen_method}'
      f'\n{"- Без использования «Решета Эратосфена»:":25} {time_find_simple_numbers}')

"""
поиск 10 числа
Затраченное время на исполнение 
- Используя алгоритм «Решето Эратосфена»: 0.1157505
- Без использования «Решета Эратосфена»: 0.06740280000000001
поиск 100 числа
Затраченное время на исполнение 
- Используя алгоритм «Решето Эратосфена»: 1.5137532
- Без использования «Решета Эратосфена»: 4.8392482999999995
поиск 1000 числа
Затраченное время на исполнение 
- Используя алгоритм «Решето Эратосфена»: 0.16941999999999968
- Без использования «Решета Эратосфена»: 7.636497599999999
Алгоритм "Решето Эратосфена" гораздо быстрее другого метода поиска больших простых чисел (больше 10).
Чем больше искомое простое число, тем больше разница во времени между обычным методом
и методом "Решето Эратосфена". Это связано с разной сложностью алгоритмов:
Без использования «Решета Эратосфена» O(n^2)
Используя алгоритм «Решето Эратосфена» O(n log(log n))
"""
