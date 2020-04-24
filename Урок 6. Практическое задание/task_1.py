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
import random
import sys
from functools import reduce

from memory_profiler import profile


@profile
def find_idx():
    numbers = [random.randint(0, 200) for i in range(60000)]
    multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]

    print(numbers)
    print('Индексы четных элементов,', multiples_idx)
    print(sys.getrefcount(multiples_idx))


find_idx()


@profile
def replace_digits():
    numbers = [random.randint(0, 200) for i in range(60000)]

    num_min = min(numbers)
    num_max = max(numbers)

    idx_min = numbers.index(num_min)
    idx_max = numbers.index(num_max)

    replace_numbers = numbers[:]
    replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
    print(numbers)
    print(replace_numbers)
    print(sys.getrefcount(replace_numbers))


replace_digits()


#обе программы работают без увеличения колва памяти