"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import time
import memory_profiler

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
    return res


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
    return primes


@memory_profiler.profile
def sequence_sum(l_sum, l_cur_num, l_count):
    if l_count > 1:
        # Результат - сумма текущего члена и всех последующих
        return l_cur_num + sequence_sum(l_sum, l_cur_num * -0.5, l_count - 1)
    else:
        return l_cur_num


if __name__ == '__main__':
    # Запускается на 64-битной Windows, Python 3.7.4
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    ##### Решето Эратосфена ######
    # Время выполнения 0.0 сек, использовано памяти 0.046875 мб
    # tmp = find_prime_number_erath(100)

    # Время выполнения 0.015625 сек, использовано памяти 0.703125 мб
    # tmp = find_prime_number_erath(1000)

    # Время выполнения 0.0625 сек, использовано памяти 3.36328125 мб
    # tmp = find_prime_number_erath(10000)

    # Время выполнения 2.046875 сек, использовано памяти 82.25 мб
    # tmp = find_prime_number_erath(100000)

    # Время выполнения 10.046875 сек, использовано памяти 403.61328125 мб
    # tmp = find_prime_number_erath(1000000)

    # Время выполнения 59.171875 сек, использовано памяти 1992.33203125 мб
    # tmp = find_prime_number_erath(2000000)
    ########################################

    #### Обычный алгоритм перебора #########
    # Время выполнения 0.0 сек, использовано памяти 0.01953125 мб
    # tmp = find_prime_number(100)

    # Время выполнения 0.0 сек, использовано памяти 0.046875 мб
    # tmp = find_prime_number(1000)

    # Время выполнения 0.078125 сек, использовано памяти 0.48828125 мб
    # tmp = find_prime_number(10000)

    # Время выполнения 2.125 сек, использовано памяти 4.328125 мб
    # tmp = find_prime_number(100000)

    # Время выполнения 57.40625 сек, использовано памяти 38.640625 мб
    # tmp = find_prime_number(1000000)

    # Время выполнения 154.625 сек, использовано памяти 76.86328125 мб
    #tmp = find_prime_number(2000000)
    ########################################
    # Вывод #
    # Как видно, решето работает быстрее, но требует гораздо больше памяти
    # Разница по скорости между обеими версиями для 2000000 меньше
    # т.к. много времени уходит на выделение памяти, вплоть до SWAP памяти

    # Не совсем понял, как профилировать рекурсивные функции
    # И столкнулся с тем, что профилировщик дополнительно вызывает функцию и происходит переполнение стека рекурсии
    # При установленом значении в 1000, запуск 990 раз допустим. Но при этом с профилировщиком уже падает ошибка, даже при 500
    count = 500
    res = sequence_sum(0, 1, count)

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Время выполнения {time_diff} сек, использовано памяти {memory_diff} мб')

