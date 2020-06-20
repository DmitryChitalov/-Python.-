"""
Скорость работы скрипта не использующий список
гораздо выше, так как любые операции со списками
будут тратить время.
"""

import timeit


def no_list(num):
    cutter = 0
    stop_count = num
    count_divider = 0
    i = 0
    while not cutter == stop_count:
        i += 1
        if count_divider == 2:
            cutter += 1
            if cutter == stop_count:
                return el
        count_divider = 0
        for el in range(1, i + 1):
            if i % el == 0 and i >= el:
                count_divider += 1


def generator_func():
    div_counter = 0
    base_num = [x for x in range(2, 30)]  # range of index
    result = []
    for i in base_num:
        for y in base_num:
            if i % y == 0 and i >= y:
                div_counter += 1
        if div_counter == 1:
            result.append(i)
        div_counter = 0
    return result[-1]


user_num = 10
user_num_2 = 10
print(f'{user_num} natural number = {no_list(user_num)}')
print(timeit.timeit(
    "no_list",
    setup="from __main__ import no_list",
    number=100)
    )
print(f'{user_num_2} natural number = {generator_func()}')
print(timeit.timeit(
    "generator_func",
    setup="from __main__ import generator_func",
    number=100)
    )
