"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
from functools import lru_cache  # импортируем модуль lru_cache - встроенный модуль мемоизации

"""
На разных входных значениях рекурсия выполняется медленее,чем цикл.
Не смотря на то,что в данном примере рекурсия и цикл имеют линейную сложность,
рекурсия выполняется медленее в связи с тем,что требует больше ресурсов
(использует стек вызовов и передает аргументы в функцию).
Большей скоростью обладает оптимизированные функции рекурсии.
Это достигается путем сохранения результата работы
функции (мемоизации) с использованием различных инструментов.
В первом примере, разница во времени выполнения зависит от длины числа,
которое мы передаем на ввод.
Также заметил,что замер через функцию показывает гораздо лучший результат
(ф-ия работает быстрее),чем просто замер через строку кода.
По моим замерам именно lru_cache имеет одну из самых высоких скоростей обработки.
Для примера оптимизации взял две задачи с рекурсией. В задачах с использованием цикла,не нашел
что можно было бы оптимизировать.
"""

# рекурсия
def reverse_func(number, reverse):
    if int(number) >= 0:
        if int(number) != 0:
            reverse *= 10
            reverse += int(number) % 10
            return reverse_func(int(number) // 10, reverse)
        return reverse


# цикл
def while_reverse(number):
    reverse = 0
    if number > 0:
        while number != 0:
            reverse *= 10
            reverse += number % 10
            number = number // 10
        return reverse


# вариант оптимизации рекурсии
# используем мемоизацию - сохранеям результат выполнения функции,
# а не считаем его каждый раз при вызове ф-ии

MEMO = {}


def reverse_func_2(number, reverse):
    if number not in MEMO and number != 0:
        reverse *= 10
        reverse += int(number) % 10
        MEMO[number] = reverse_func_2(int(number) // 10, reverse)
        return MEMO[number]
    return reverse


# также можно использовать универсальный декоратор для любого количества аргументов
def memoize(f):
    cache = {}

    def decorate(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return decorate


@memoize
def reverse_func_3(number, reverse):
    if int(number) >= 0:
        if int(number) != 0:
            reverse *= 10
            reverse += int(number) % 10
            return reverse_func_3(int(number) // 10, reverse)
        return reverse


# подобный декоратор реализован в стандартной библиотеке functools - lru_cache()

@lru_cache()
def reverse_func_4(number, reverse):
    if int(number) >= 0:
        if int(number) != 0:
            reverse *= 10
            reverse += int(number) % 10
            return reverse_func_4(int(number) // 10, reverse)
        return reverse


print(f'Время работы обычной рекурсии :'
      f'{timeit.timeit("reverse_func(1234567,reverse=0)", setup="from __main__ import reverse_func", number=1000)}')
print(f'Время работы цикла :'
      f'{timeit.timeit("while_reverse(1234567)", setup="from __main__ import while_reverse", number=1000)}')
print(f'Время работы оптимизированной ф-ии :'
      f'{timeit.timeit("reverse_func_2(1234567,reverse=0)", setup="from __main__ import reverse_func_2", number=1000)}')
print(f'Время работы ф-ии с использованием универсального декоратора :'
      f'{timeit.timeit("reverse_func_3(1234567,reverse=0)", setup="from __main__ import reverse_func_3", number=1000)}')
print(f'Время работы ф-ии с использованием декоратора lru_cache из стандартной библиотеки functools:'
      f'{timeit.timeit("reverse_func_4(1234567,reverse=0)", setup="from __main__ import reverse_func_4", number=1000)}')


# замеры и вариант оптимизации через мемоизацию второй задачи с рекурсией

def even_count(number, even_score, not_even_score):
    if int(number) > 0 and int(number) % 2 == 0:
        even_score += 1
        return even_count(number // 10, even_score, not_even_score)
    if int(number) > 0:
        not_even_score += 1
        return even_count(number // 10, even_score, not_even_score)
    return f'Количество четных' \
            f' и нечетных цифр в числе равно: ({even_score}, {not_even_score})'

# используем универсальный декоратор

def memoize(f):
    cache = {}

    def decorate(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return decorate

@memoize
def even_count_2(number, even_score, not_even_score):
    if int(number) > 0 and int(number) % 2 == 0:
        even_score += 1
        return even_count_2(number // 10, even_score, not_even_score)
    if int(number) > 0:
        not_even_score += 1
        return even_count_2(number // 10, even_score, not_even_score)
    return f'Количество четных' \
            f' и нечетных цифр в числе равно: ({even_score}, {not_even_score})'


print(f'Время работы второй задачи (рекурсия):'
      f'{timeit.timeit("even_count(123, even_score=0, not_even_score=0)", setup="from __main__ import even_count", number=10000)}')
print(f'Время работы второй задачи с использованием декоратора @memoize :'
      f'{timeit.timeit("even_count_2(123, even_score=0, not_even_score=0)", setup="from __main__ import even_count_2", number=10000)}')
